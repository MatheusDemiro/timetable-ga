from copy import deepcopy

import numpy.random as npr
import random

from models.evaluation import Evaluation
from settings import LESSONS_PER_DAY, WEEK_SIZE


class GeneticAlgorithm:
    def __init__(self, population):
        self.population = population

    def crossover(self, child, parent_x, parent_y, period):
        selection_matrix = self.generate_selection_matrix()
        non_inherited_lessons = []
        for column in range(WEEK_SIZE):
            for row in range(LESSONS_PER_DAY):
                if selection_matrix[column][row]:
                    child.individual[period][column][row] = parent_x[column][row]
                else:
                    non_inherited_lessons.append(parent_x[column][row])

        new_parent_y = self.order(non_inherited_lessons, parent_y)

        # TO-DO: adicionar as turmas de "new_parent_y" ao filho ("child")
        print(new_parent_y)

    def mutation(self):
        pass

    def parent_selection(self):
        parent_x = deepcopy(self.roulette_wheel_selection())
        parent_y = deepcopy(self.roulette_wheel_selection())

        return parent_x, parent_y

    def roulette_wheel_selection(self):
        population_fitness = sum([individual.fitness for individual in self.population.individuals])

        individual_probabilities = [individual.fitness/population_fitness for individual in self.population.individuals]

        return npr.choice(self.population.individuals, p=individual_probabilities)

    def order(self, non_inherited_lessons, parent):
        ordered_list = []
        for column in range(WEEK_SIZE):
            for row in range(LESSONS_PER_DAY):
                if self.find_lesson(parent[column][row], non_inherited_lessons):
                    ordered_list.append(parent[column][row])

        return ordered_list

    @staticmethod
    def find_lesson(lesson, lessons):
        result = False
        for i in range(len(lessons)):
            if lesson is not None and lessons[i] is not None:
                if lesson.id == lessons[i].id:
                    del lessons[i]
                    result = True
                    break
            elif lesson is None:
                if lesson == lessons[i]:
                    del lessons[i]
                    result = True
                    break

        return result

    @staticmethod
    def generate_selection_matrix():
        matrix = []
        for column in range(WEEK_SIZE):
            element = []
            for row in range(LESSONS_PER_DAY):
                element.append(random.randint(0, 1))
            matrix.append(element)
        return matrix

    @staticmethod
    def generate_individual_matrix():
        matrix = []
        for column in range(WEEK_SIZE):
            element = []
            for row in range(LESSONS_PER_DAY):
                element.append(None)
            matrix.append(element)
        return matrix


