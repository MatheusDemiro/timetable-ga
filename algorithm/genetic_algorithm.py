from copy import deepcopy

import numpy.random as npr
import random

from settings import LESSONS_PER_DAY, WEEK_SIZE


class GeneticAlgorithm:
    def __init__(self, population):
        self.population = population
        self.population_fitness = sum([individual.fitness for individual in self.population.individuals])
        self.individual_probabilities = [individual.fitness / self.population_fitness for individual in
                                         self.population.individuals]

    def crossover(self, child, parent_x, parent_y, period):
        selection_matrix = self.generate_selection_matrix()
        non_inherited_lessons = []
        for column in range(WEEK_SIZE):
            for row in range(LESSONS_PER_DAY):
                if selection_matrix[column][row]:
                    child.individual[period][column][row] = parent_x[column][row]
                else:
                    child.individual[period][column][row] = 0
                    non_inherited_lessons.append(parent_x[column][row])

        new_parent_y = self.order(non_inherited_lessons, parent_y)

        # Inserindo em ordem as características não herdadas do parent_x
        self.inherit_from_second_parent(child, new_parent_y, period)

        # Realizando a mutação do filho gerado (correção de anomalias)
        self.mutation(child, period)

        child.calculate_fitness()

    def mutation(self, child, period):
        # Corrigindo intervalos vagos entre aulas
        child.fix_empty_lessons(period)

        # Corrigindo aulas sequenciais no mesmo dia de uma disciplina
        child.fix_lessons_same_day(period)

    def parent_selection(self):
        parent_x = deepcopy(self.roulette_wheel_selection())
        parent_y = deepcopy(self.roulette_wheel_selection())

        return parent_x, parent_y

    def roulette_wheel_selection(self):
        return npr.choice(self.population.individuals, p=self.individual_probabilities)

    def order(self, non_inherited_lessons, parent):
        ordered_list = []
        for column in range(WEEK_SIZE):
            for row in range(LESSONS_PER_DAY):
                if self.find_lesson(parent[column][row], non_inherited_lessons):
                    ordered_list.append(parent[column][row])

        return ordered_list

    @staticmethod
    def inherit_from_second_parent(child, parent_y, period):
        index = 0
        for column in range(len(child.individual[period])):
            for row in range(len(child.individual[period][0])):
                if child.individual[period][column][row] == 0:
                    child.individual[period][column][row] = parent_y[index]
                    index += 1

    @staticmethod
    def find_lesson(lesson, lessons):
        result = False
        for index in range(len(lessons)):
            if lesson is not None and lessons[index] is not None:
                if lesson.id == lessons[index].id:
                    del lessons[index]
                    result = True
                    break
            elif lesson is None:
                if lesson == lessons[index]:
                    del lessons[index]
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
