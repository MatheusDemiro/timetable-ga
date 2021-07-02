import matplotlib.pyplot as plt


class Graphics:
    def __init__(self, average_fitness=None, low_fitness_individuals=None):
        if low_fitness_individuals is None:
            low_fitness_individuals = []
        if average_fitness is None:
            average_fitness = []
        self.average_fitness = average_fitness
        self.low_fitness_individuals = low_fitness_individuals

    def show_average_fitness(self):
        axis_x = [i + 1 for i in range(len(self.average_fitness))]

        print("MÉDIA (VARIAÇÃO): %f - %f" % (min(self.average_fitness),
                                             max(self.average_fitness)))

        self.show_graphic(axis_x, self.average_fitness, "Média de aptidão das gerações", "Geração", "Aptidão média",
                          './figures/average_fitness.png')

    def show_average_individuals_low_fitness(self):
        axis_x = [i + 1 for i in range(len(self.low_fitness_individuals))]

        print("PIOR INDIVÍDUO (VARIAÇÃO): %f - %f" % (min(self.low_fitness_individuals),
                                                      max(self.low_fitness_individuals)))

        self.show_graphic(axis_x, self.low_fitness_individuals, "Aptidão dos piores indivíduos", "Geração", "Aptidão",
                          './figures/low_fitness_individuals.png')

    @staticmethod
    def show_graphic(axis_x, axis_y, title, x_label, y_label, filename):
        plt.plot(axis_x, axis_y, marker="o")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.savefig(filename)

        plt.show()
