from random import randint
from chromosome import Chromosome

paths = []
vertices = []

'''
    .fit_score()
    Elementos que tenham mais de uma visita ao mesmo nó, será penalizado com score negativo.
'''


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
    population = fit_score(population)
    print(*[x for x in population if not x.monster ], sep='\n')


if __name__ == "__main__":
    main()
