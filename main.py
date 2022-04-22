import time
import gc

from algorithm.genetic_algorithm import GeneticAlgorithm
from algorithm.graphics import Graphics
from models.evaluation import Evaluation
from models.population import Population
from settings import GENERATIONS_NUMBER
from utils import Utils


# Atualmente esse algoritmo considera que os professores não possuem dedicação exclusiva, levando em consideração a
# disponibilidade e a preferência de horário do professor


def save_best_individuals(population):
    arq = open("files/%s.txt" % Utils.get_filename(), "w+")
    individuals = []
    for individual in population.individuals:
        if individual not in individuals and individual.fitness == 2:
            individuals.append(individual)
    schedule = 1
    for individual in individuals:
        timetable = Utils.get_timetable(individual)
        arq.writelines("Individual %d\n" % schedule)
        for item in timetable:
            arq.write(item.get_string())
            arq.writelines("\n")
        arq.writelines("\n")
        schedule += 1
    arq.close()


actual_population = Population()

start = time.time()

generation_number = 0
count_best_individual = 0

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

        best_individual = child

    actual_population = genetic_algorithm.selection_of_survivors(newPopulation)

    best_individual = max(actual_population.individuals, key=lambda x: x.fitness)

    best_individuals.append(best_individual)

    average = sum(individual.fitness for individual in actual_population.individuals) / actual_population.size

    average_fitness.append(average)

    low_fitness_individuals.append(min(actual_population.individuals, key=lambda x: x.fitness).fitness)

    generation_number += 1
    end_generation = time.time()

    print("TEMPO DE EXECUÇÃO PARA A GERAÇÃO %i - Tempo: %f - Melhor indivíduo: %f - Média: %f" %
          (generation_number, end_generation - start_generation, best_individual.fitness, average))

    gc.collect()

    # Parando execução após encontrar indivíduo com fitness 2
    if best_individual.fitness == 2:
        count_best_individual += 1
        if count_best_individual == 30 or generation_number == GENERATIONS_NUMBER:
            save_best_individuals(actual_population)
            break

end = time.time()

print("TEMPO DE EXECUÇÃO %f" % (end - start))
print("\n")

graphics = Graphics(average_fitness=average_fitness, low_fitness_individuals=low_fitness_individuals)

graphics.show_average_fitness()
graphics.show_average_individuals_low_fitness()

print("\n")

# Melhor indivíduo de todas as gerações
Utils.print_timetable(best_individual)
Utils.print_best_individual(best_individual)

generation = 1
for i in best_individuals:
    print("Melhor indivíduo da geração %i: %.4f" % (generation, i.fitness))
    generation += 1

