import random

from database.database import Database
from models.evaluation import Evaluation
from settings import TOTAL_PERIODS, LESSONS_PER_DAY, WEEK_SIZE, POPULATION_SIZE


class Population:
    def __init__(self, size=POPULATION_SIZE):
        self.size = size
        self.database = Database()
        self.individuals = []

        self.initialize()

    # @staticmethod
    # def get_lesson_of_day(lesson_list):
    #     lessons_of_day = [None] * LESSONS_PER_DAY
    #     for i in range(LESSONS_PER_DAY):
    #         if len(lesson_list) > 0:
    #             index = random.randrange(len(lesson_list))
    #             lesson = lesson_list[index]
    #             if lesson.subject.lessons_per_week > 0:
    #                 lesson.subject.lessons_per_week -= 1
    #                 lessons_of_day[i] = lesson
    #
    #                 if lesson.subject.lessons_per_week == 0:
    #                     del lesson_list[index]
    #
    #     return lessons_of_day

    @staticmethod
    def get_lesson_of_day(lesson_list):
        lessons_of_day = [None] * LESSONS_PER_DAY
        for i in range(LESSONS_PER_DAY):
            index = random.randrange(len(lesson_list))
            lesson = lesson_list[index]
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
        for size in range(POPULATION_SIZE):
            evaluation = Evaluation(individual=[])
            for period in range(TOTAL_PERIODS):
                lessons = list(filter(lambda x: x.subject.period == period + 1, self.database.get_lessons()))
                evaluation.individual.append(self.generate_individual(lessons))

            evaluation.calculate_fitness()
            self.individuals.append(evaluation)
