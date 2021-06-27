from prettytable import PrettyTable

from population import Population
from settings import LESSONS_PER_DAY


# Atualmente esse algoritmo considera que os professores possuem dedicação exclusiva apenas para um determinado curso,
# ou seja, não leva em consideração a disponibilidade e nem a preferência de horário do professor


def printTimetable(periods):
    for period in periods:
        table = PrettyTable(['seg', 'ter', 'qua', 'qui', 'sex'])
        for j in range(LESSONS_PER_DAY):
            table.add_row([period[0][j].subject.code if period[0][j] is not None else None,
                           period[1][j].subject.code if period[1][j] is not None else None,
                           period[2][j].subject.code if period[2][j] is not None else None,
                           period[3][j].subject.code if period[3][j] is not None else None,
                           period[4][j].subject.code if period[4][j] is not None else None])

        print(table)


population = Population()

for key in population.periods:
    print("--------------------------Geração Período %d--------------------------" % key)
    printTimetable(population.periods[key][0])
