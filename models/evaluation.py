import itertools
import random

from settings import WEEK_SIZE, LESSONS_PER_DAY, TOTAL_PERIODS


class Evaluation:
    def __init__(self, individual=None):
        if individual is None:
            individual = [[[None for i in range(3)] for j in range(5)] for k in range(TOTAL_PERIODS)]
        self.individual = individual
        self.fitness = -1

    def calculate_fitness(self):
        """
        :return: 1/((summation[x, p=1](ap + vp + up + lp)) + (ch * k)) -> quantidade de infrações do indivíduo
        """
        summation = 0
        for period in self.individual:
            ap = self.sum_empty_lessons_first_time(period)
            vp = self.sum_empty_lessons_between_lessons(period)
            up = self.sum_lessons_only_last_time(period)
            lp = self.sum_lessons_same_day(period)

            summation += ap + vp + up + lp

        ch = self.sum_timing_clashes_between_periods()
        k = 10

        summation += (ch * k)

        if summation > 0:
            self.fitness = 1 / summation
        elif summation == 0:
            self.fitness = 2.0

    def fix_empty_lessons(self, period):
        """
        Correção de intervalos vagos e de dias com aulas apenas no último horário
        :param period: índice do período
        :return: None
        """
        for lessons_of_day in self.individual[period]:
            if lessons_of_day[0] is not None and lessons_of_day[1] is None and lessons_of_day[2] is not None:
                lessons_of_day[1] = lessons_of_day[2]
                lessons_of_day[2] = None

            if lessons_of_day[0] is None and lessons_of_day[1] is None and lessons_of_day[2] is not None:
                lessons_of_day[1] = lessons_of_day[2]
                lessons_of_day[2] = None

            if lessons_of_day[0] is None and lessons_of_day[1] is not None:
                lessons_of_day[0] = lessons_of_day[1]
                lessons_of_day[1] = lessons_of_day[2]
                lessons_of_day[2] = None

    def fix_lessons_same_day(self, period):
        """
        Correção de aulas sequenciais de uma mesma disciplina no mesmo dia
        :param period: índice do período
        :return: None
        """
        for day in range(WEEK_SIZE):
            lessons_of_day = self.individual[period][day]
            for index_x, index_y in itertools.combinations(range(LESSONS_PER_DAY), 2):
                lesson_x, lesson_y = lessons_of_day[index_x], lessons_of_day[index_y]
                if lessons_of_day[index_x] is not None and lessons_of_day[index_y] is not None:
                    if lesson_x.id == lesson_y.id:
                        # Selecionar turmas do período que não sejam ministradas pelo professor
                        lessons = self.get_non_teacher_lessons(lesson_x.teacher, period, day)

                        # Selecionando aleatoriamente um elemento da "lessons"
                        position = lessons[random.randrange(len(lessons))]
                        lesson = self.individual[period][position[0]][position[1]]

                        # Trocando turmas de dia (lesson_x e lesson)
                        aux = lesson
                        self.individual[period][position[0]][position[1]] = lesson_x
                        self.individual[period][day][index_x] = aux

    def fix_timing_clashes(self, period_x, period_y):
        for column in range(WEEK_SIZE):
            for row in range(LESSONS_PER_DAY):
                lesson_x = period_x[column][row]
                lesson_y = period_y[column][row]
                random_index = random.randint(0, 1)
                if lesson_x is not None and lesson_y is not None:
                    if lesson_x.teacher.id == lesson_y.teacher.id:
                        if random_index == 0:
                            # Definindo listas de prioridades considerando period_x
                            empty_lessons_first_time, empty_lessons_second_time, lessons = self.get_priorities(period_x)

                            # Aplicando prioridades
                            self.apply_priorities(period_x, empty_lessons_first_time, empty_lessons_second_time, lessons,
                                                  (column, row))
                        else:
                            # Definindo listas de prioridades considerando period_y
                            empty_lessons_first_time, empty_lessons_second_time, lessons = self.get_priorities(period_y)

                            # Aplicando prioridades
                            self.apply_priorities(period_y, empty_lessons_first_time, empty_lessons_second_time, lessons,
                                                  (column, row))

    def apply_priorities(self, period, priorities_1, priorities_2, priorities_3, indexes):
        """
        Corrigindo o choque de horários baseado nas prioridades
        :param period: matriz com as turmas do período
        :param priorities_1: lista de prioridade primária
        :param priorities_2: lista de prioridade secundária
        :param priorities_3: lista de prioridade terciária
        :param indexes: tupla (column, row) com a posição do elemento a ser alterado
        :return: None
        """
        if len(priorities_1) > 0:
            # Usar primeira lista de prioridade (aulas vagas no primeiro horário)
            self.changed_lessons(period, priorities_1, indexes)
        elif len(priorities_2) > 0:
            # Usar segunda lista de prioridade (aulas vagas no segundo horário)
            self.changed_lessons(period, priorities_2, indexes)
        else:
            # User terceira lista de prioridade (aulas restantes)
            self.changed_lessons(period, priorities_3, indexes)

    @staticmethod
    def changed_lessons(period, items, indexes):
        """
        Função que executa a troca de elementos entre :items e :period
        :param period: matriz com itens originais do problema
        :param items: iterável com tuplas de índices
        :param indexes: tupla (column, row) com a posição do elemento a ser alterado
        :return: None
        """
        random_lesson = items[random.randrange(len(items))]
        aux = period[indexes[0]][indexes[1]]
        period[indexes[0]][indexes[1]] = period[random_lesson[0]][random_lesson[1]]
        period[random_lesson[0]][random_lesson[1]] = aux

    @staticmethod
    def get_priorities(period):
        empty_lessons_first_time = []
        empty_lessons_second_time = []
        lessons = []

        for column in range(WEEK_SIZE):
            if period[column][0] is None:
                empty_lessons_first_time.append((column, 0))
            if period[column][1] is None:
                empty_lessons_second_time.append((column, 1))
            for row in range(LESSONS_PER_DAY):
                if row <= 1:
                    if period[column][row] is not None:
                        lessons.append((column, row))
                else:
                    lessons.append((column, row))

        return empty_lessons_first_time, empty_lessons_second_time, lessons

    def get_non_teacher_lessons(self, teacher, period, day):
        lessons = []
        for column in range(WEEK_SIZE):
            if column != day:
                for row in range(LESSONS_PER_DAY):
                    lesson = self.individual[period][column][row]
                    if lesson is None:
                        lessons.append((column, row, lesson))
                    elif lesson.teacher.id != teacher.id and \
                            not self.check_lesson_in_day(self.individual[period][column], lesson.id):
                        lessons.append((column, row, lesson))

        return lessons

    @staticmethod
    def check_lesson_in_day(lessons_of_day, lesson_id):
        for lesson in lessons_of_day:
            if lesson is not None and lesson.id == lesson_id:
                return True
        return False

    @staticmethod
    def sum_empty_lessons_first_time(period):
        """
        :param period: objeto período
        :return: quantidade de aulas vagas no primeiro horário, desde que possua aula no segundo horário
        """
        total = 0
        for lessons_of_day in period:
            if lessons_of_day[0] is None and lessons_of_day[1] is not None:
                total += 1

        return total

    @staticmethod
    def sum_empty_lessons_between_lessons(period):
        """
        :param period: objeto período
        :return: quantidade de aulas vagas entre aulas
        """
        total = 0
        for lessons_of_day in period:
            if lessons_of_day[0] is not None and lessons_of_day[1] is None and lessons_of_day[2] is not None:
                total += 1

        return total

    @staticmethod
    def sum_lessons_only_last_time(period):
        """
        :param period: objeto período
        :return: quantidade de aulas que são ofertadas apenas no último horário
        """
        total = 0
        for lessons_of_day in period:
            if lessons_of_day[0] is None and lessons_of_day[1] is None and lessons_of_day[2] is not None:
                total += 1

        return total

    @staticmethod
    def sum_lessons_same_day(period):
        total = 0
        for day in range(WEEK_SIZE):
            lessons_of_day = period[day]
            for index_x, index_y in itertools.combinations(range(LESSONS_PER_DAY), 2):
                lesson_x, lesson_y = lessons_of_day[index_x], lessons_of_day[index_y]
                if lessons_of_day[index_x] is not None and lessons_of_day[index_y] is not None:
                    if lesson_x.id == lesson_y.id:
                        total += 1
        return total

    def sum_timing_clashes_between_periods(self):
        """
        :return: quantidade de choques de horários entre os períodos
        """
        total = 0
        for period_index in range(len(self.individual)):
            for p in range(period_index + 1, len(self.individual)):
                total += self.verify_timing_clashes(self.individual[period_index], self.individual[p])

        return total

    @staticmethod
    def verify_timing_clashes(matrix_1, matrix_2):
        total = 0
        for column in range(WEEK_SIZE):
            for row in range(LESSONS_PER_DAY):
                lesson_1 = matrix_1[column][row]
                lesson_2 = matrix_2[column][row]
                if lesson_1 is not None and lesson_2 is not None:
                    if lesson_1.teacher.id == lesson_2.teacher.id:
                        total += 1

        return total
