from prettytable import PrettyTable

from algorithm.genetic_algorithm import GeneticAlgorithm
from models.evaluation import Evaluation
from population import Population
from settings import LESSONS_PER_DAY, GENERATIONS_NUMBER, TOTAL_PERIODS


# Atualmente esse algoritmo considera que os professores possuem dedicação exclusiva apenas para um determinado curso,
# ou seja, não leva em consideração a disponibilidade e nem a preferência de horário do professor
# Na versão 2 o algoritmo considera um indivíduo como sendo o conjunto de períodos


def printTimetable(evaluation):
    for period in evaluation.individual:
        table = PrettyTable(['seg', 'ter', 'qua', 'qui', 'sex'])
        for j in range(LESSONS_PER_DAY):
            table.add_row([period[0][j].subject.code if period[0][j] is not None else None,
                           period[1][j].subject.code if period[1][j] is not None else None,
                           period[2][j].subject.code if period[2][j] is not None else None,
                           period[3][j].subject.code if period[3][j] is not None else None,
                           period[4][j].subject.code if period[4][j] is not None else None])

        print(table)


population = Population()
genetic_algorithm = GeneticAlgorithm(population)

generation_number = 0
while generation_number < GENERATIONS_NUMBER:
    # Os operadores genéticos são aplicados em toda a população (repetição do tamanho da população)
    newPopulation = Population()
    for i in range(population.size):
        # Seleção dos pais
        parent_x, parent_y = genetic_algorithm.parent_selection()
        child = Evaluation()
        for period in range(TOTAL_PERIODS):
            # Recombinação genética com taxa de 100% para os indivíduos do mesmo período
            genetic_algorithm.crossover(child, parent_x.individual[period], parent_y.individual[period], period)

        child = genetic_algorithm.crossover(parent_x, parent_y)
        # TO-DO: Realizar mutação
        newPopulation.individuals.append(child)

    for individual in population.individuals:
        printTimetable(individual)
        print(individual.fitness)
    generation_number += 1
