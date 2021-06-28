from settings import WEEK_SIZE, LESSONS_PER_DAY, TOTAL_PERIODS


class Evaluation:
    def __init__(self, individual=None):
        if individual is None:
            individual = [[[None for i in range(3)] for j in range(5)] for k in range(TOTAL_PERIODS)]
        self.individual = individual
        self.fitness = -1

    def calculate_fitness(self):
        """
        :return: 1/((summation[x, p=1](ap + vp + up)) + ch) -> quantidade de infrações do indivíduo
        """
        summation = 0
        for period in self.individual:
            ap = self.sum_empty_lessons_first_time(period)
            vp = self.sum_empty_lessons_between_lessons(period)
            up = self.sum_lessons_only_last_time(period)

            summation += ap + vp + up

        ch = self.sum_timing_clashes_between_periods()

        summation += ch

        if summation > 0:
            self.fitness = 1/summation
        elif summation == 0:
            self.fitness = 1.0

    @staticmethod
    def sum_empty_lessons_first_time(period):
        """
        :param period:
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
        :param period:
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
        :param period:
        :return: quantidade de aulas que são ofertadas apenas no último horário
        """
        total = 0
        for lessons_of_day in period:
            if lessons_of_day[0] is None and lessons_of_day[1] is None and lessons_of_day[2] is not None:
                total += 1

        return total

    def sum_timing_clashes_between_periods(self):
        """
        :return: quantidade de choques de horários entre os períodos
        """
        total = 0
        for period_index in range(len(self.individual)):
            for p in range(period_index+1, len(self.individual)):
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
