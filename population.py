import random

from database.database import Database
from models.evaluation import Evaluation
from models.lesson import Lesson
from models.subject import Subject
from settings import TOTAL_PERIODS, LESSONS_PER_DAY, WEEK_SIZE, POPULATION_SIZE


class Population:
    def __init__(self, size=POPULATION_SIZE):
        self.size = size
        self.database = Database()
        self.individuals = []

        self.initialize()

    def __eq__(self, other):
        return self.individuals == other.individuals

    @staticmethod
    def get_lesson_of_day(lesson_list):
        lessons_of_day = [None] * LESSONS_PER_DAY
        for i in range(LESSONS_PER_DAY):
            if len(lesson_list) > 0:
                index = random.randrange(len(lesson_list))
                lesson = lesson_list[index]
                if lesson.subject.lessons_per_week > 0:
                    lesson.subject.lessons_per_week -= 1
                    if lesson.subject.id is None:
                        lessons_of_day[i] = None
                    else:
                        lessons_of_day[i] = lesson

                    if lesson.subject.lessons_per_week == 0:
                        del lesson_list[index]

        return lessons_of_day

    def generate_individual(self, lessons):
        individual = []
        for day in range(WEEK_SIZE):
            lessons_of_day = self.get_lesson_of_day(lessons)
            individual.append(lessons_of_day)

        return individual

    def initialize(self):
        for size in range(self.size):
            evaluation = Evaluation(individual=[])
            for period in range(TOTAL_PERIODS):
                lessons = list(filter(lambda x: x.subject.period == period + 1, self.database.get_lessons()))
                self.empty_lessons(lessons)
                evaluation.individual.append(self.generate_individual(lessons))

            evaluation.calculate_fitness()
            self.individuals.append(evaluation)

    @staticmethod
    def empty_lessons(lessons):
        total_lessons_per_week = 0
        for lesson in lessons:
            total_lessons_per_week += lesson.subject.lessons_per_week

        lesson = Lesson(subject=Subject(code="NONE", name="NONE", lessons_per_week=abs((WEEK_SIZE * LESSONS_PER_DAY) -
                                                                                       total_lessons_per_week)))

        lessons.append(lesson)
