import time

from prettytable import PrettyTable

from algorithm.genetic_algorithm import GeneticAlgorithm
from algorithm.graphics import Graphics
from models.evaluation import Evaluation
from population import Population
from settings import LESSONS_PER_DAY, GENERATIONS_NUMBER


# Atualmente esse algoritmo considera que os professores possuem dedicação exclusiva apenas para um determinado curso,
# ou seja, não leva em consideração a disponibilidade e nem a preferência de horário do professor
# Na versão 2 o algoritmo considera um indivíduo como sendo o conjunto de períodos


def print_timetable(evaluation):
    for period in evaluation.individual:
        table = PrettyTable(['seg', 'ter', 'qua', 'qui', 'sex'])
        for j in range(LESSONS_PER_DAY):
            table.add_row([period[0][j].subject.code if period[0][j] is not None else None,
                           period[1][j].subject.code if period[1][j] is not None else None,
                           period[2][j].subject.code if period[2][j] is not None else None,
                           period[3][j].subject.code if period[3][j] is not None else None,
                           period[4][j].subject.code if period[4][j] is not None else None])

        print(table)


actual_population = Population()

start = time.time()

generation_number = 0

average_fitness = []
low_fitness_individuals = []
best_individuals = []

best_individual = None
while generation_number < GENERATIONS_NUMBER:
    start_generation = time.time()
    genetic_algorithm = GeneticAlgorithm(actual_population)

    newPopulation = Population(size=0)
    newPopulation.size = actual_population.size
    for i in range(actual_population.size):
        # Seleção dos pais
        parent_x, parent_y = genetic_algorithm.parent_selection()

        # Filho
        child = Evaluation()

        # Recombinação genética com taxa de 100% para os indivíduos do mesmo período
        genetic_algorithm.crossover(child, parent_x, parent_y)

        # Recalculando fitness após crossover
        child.calculate_fitness()

        # Realizar mutação de todos os indivíduos
        genetic_algorithm.mutation(child)

        # Recalculando fitness após mutação
        child.calculate_fitness()

        newPopulation.individuals.append(child)

    actual_population = genetic_algorithm.selection_of_survivors(newPopulation)

    best_individual = max(actual_population.individuals, key=lambda x: x.fitness)

    best_individuals.append(best_individual)

    average_fitness.append(sum(individual.fitness for individual in actual_population.individuals) /
                           actual_population.size)
    low_fitness_individuals.append(min(actual_population.individuals, key=lambda x: x.fitness).fitness)

    generation_number += 1
    end_generation = time.time()

    # print("TEMPO DE EXECUÇÃO PARA A GERAÇÃO %i - %f" % (generation_number, end_generation - start_generation))

end = time.time()

print("TEMPO DE EXECUÇÃO %f" % (end - start))
print("\n")

graphics = Graphics(average_fitness=average_fitness, low_fitness_individuals=low_fitness_individuals)

graphics.show_average_fitness()
graphics.show_average_individuals_low_fitness()

print("\n")

# Melhor indivíduo de todas as gerações
print_timetable(best_individual)
print("\nAPTIDÃO DO MELHOR INDIVÍDUO: %.4f" % best_individual.fitness)

generation = 1
for i in best_individuals:
    print("Melhor indivíduo da geração %i: %.4f" % (generation, i.fitness))
    generation += 1

