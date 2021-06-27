import random

from database.database import Database
from settings import PERIOD_QUANTITY, LESSONS_PER_DAY, WEEK_SIZE, POPULATION_SIZE


class Population:
    def __init__(self, size=POPULATION_SIZE):
        self.size = size
        self.database = Database()
        self.periods = {i+1: [] for i in range(PERIOD_QUANTITY)}

        self.initialize()

    @staticmethod
    def get_lesson_of_day(lesson_list):
        lessons_of_day = [None] * LESSONS_PER_DAY
        for i in range(LESSONS_PER_DAY):
            lesson = lesson_list[random.randrange(len(lesson_list))]
            if lesson.subject.lessons_per_week > 0:
                lesson.subject.lessons_per_week -= 1
                lessons_of_day[i] = lesson

        return lessons_of_day

    def generate_individual(self, lessons):
        individual = []
        for day in range(WEEK_SIZE):
            lessons_of_day = self.get_lesson_of_day(lessons)
            individual.append(lessons_of_day)

        return individual

    def initialize(self):
        for period in range(PERIOD_QUANTITY):
            generations = []
            for size in range(POPULATION_SIZE):
                lessons = list(filter(lambda x: x.subject.period == period + 1, self.database.get_lessons()))
                individual = self.generate_individual(lessons)

                generations.append(individual)

            self.periods[period+1].append(generations)

    def fitness(self, individual):
        """ Return 1/((somatório[x, p=1](ap + vp + up)) + ch) """

        # calcular quantidade de aulas vagas no primeiro horário
        # calcular quantidade de aulas vagas entre aulas
        # calcular quantidade de aulas que são ofertadas apenas no último horário
        # calcular quantidade de choques de horários entre os períodos
