from random import randint
from functools import cmp_to_key
from chromosome import Chromosome

paths = []
vertices = []
crossover_rate = 0.6
mutation_rate = 0.05
generation = 0
the_best = Chromosome([])


def fit_score(population):
    for elem in population:
        elem.cities_count = [0] * len(vertices)
        for index, x in enumerate(elem.path):
            if x == 1:
                for v in paths[index]:
                    elem.cities_count[vertices.index(v)] += 1
                    elem.score += 1
                    if elem.cities_count[vertices.index(v)] > 2:
                        elem.monster = True
                        elem.score = -1
                        break
                else:
                    continue
                break

    return population


def crossover(population):
    new_population = []
    for x in population:
        for y in population:
            if x != y:
                path = []
                path2 = []
                for index, k in enumerate(x.path):
                    choice = randint(0, 1)
                    if choice == 1:
                        path.append(x.path[index])
                        path2.append(y.path[index])
                    else:
                        path.append(y.path[index])
                        path2.append(x.path[index])

                specimen = Chromosome(path)
                new_population.append(specimen)
                specimen = Chromosome(path2)
                new_population.append(specimen)

    return new_population


def mutation(population):
    size = len(population)
    if size > 50:
        rate = max(3, int(size * mutation_rate))

        for i in range(rate):
            index = randint(0, size - 1)
            path = population[index].path
            for index, k in enumerate(path):
                change = randint(0, 9)
                if change == 5:
                    if k == 0:
                        path[index] = 1
                    else:
                        path[index] = 0

            population[index].path = path

    return population


def selection(population):
    population = fit_score(population)
    population = [x for x in population if not x.monster]
    population = sorted(population, key=cmp_to_key(Chromosome.comparator))

    global the_best
    the_best = population[0]

    size = len(population)
    rate = min(50, int(size * crossover_rate))
    new_population = crossover(population[:rate])

    population = population + new_population

    global generation
    generation += 1

    return population


def main():
    n_path = int(input("Numero de caminhos: "))

    for _ in range(n_path):
        path = input()
        for x in path:
            if x not in vertices:
                vertices.append(x)

        paths.append(path)

    population = []
    for i in range(100 * len(vertices)):
        path = []
        for x in range(n_path):
            path.append(randint(0, 1))
        chromosome = Chromosome(path)
        population.append(chromosome)

    while the_best.score / 2 < len(vertices):
        selection(population)
        print("Geração: " + str(generation))
        print("Melhor cromossomo: " + str(the_best))
        print()


if __name__ == "__main__":
    main()
