from datetime import datetime

from prettytable import PrettyTable

from settings import SAMPLE_NAME, LESSONS_PER_DAY


class Utils:
    @staticmethod
    def print_best_individual(best_individual):
        print("\nAPTIDÃO DO MELHOR INDIVÍDUO: %.4f" % best_individual.fitness)
        print("\nCOMPONENTES FITNESS:")
        print("\t ap: %s" % best_individual.summation['ap'])
        print("\t vp: %s" % best_individual.summation['vp'])
        print("\t up: %s" % best_individual.summation['up'])
        print("\t lp: %s" % best_individual.summation['lp'])
        print("\t pf: %s" % best_individual.summation['pf'])
        print("\t ch: %s" % best_individual.summation['ch'])
        print("\t Total: %i" % ((sum(best_individual.summation.values()) - best_individual.summation['ch']) +
                                (best_individual.summation['ch'] * 10)))

    @staticmethod
    def generate_pretty_table(period):
        table = PrettyTable(['seg', 'ter', 'qua', 'qui', 'sex'])
        for j in range(LESSONS_PER_DAY):
            table.add_row([period[0][j].subject.code if period[0][j] is not None else None,
                           period[1][j].subject.code if period[1][j] is not None else None,
                           period[2][j].subject.code if period[2][j] is not None else None,
                           period[3][j].subject.code if period[3][j] is not None else None,
                           period[4][j].subject.code if period[4][j] is not None else None])
        return table

    @staticmethod
    def print_timetable(evaluation):
        for period in evaluation.individual:
            table = Utils.generate_pretty_table(period)
            print(table)

    @staticmethod
    def get_timetable(evaluation):
        timetable = []
        for period in evaluation.individual:
            timetable.append(Utils.generate_pretty_table(period))
        return timetable

    @staticmethod
    def get_datetime_now():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    @staticmethod
    def get_formatted_datetime_now():
        return datetime.now().strftime("%d%m%Y%H%M%S")

    @staticmethod
    def get_filename():
        return SAMPLE_NAME + "_" + Utils.get_formatted_datetime_now()
