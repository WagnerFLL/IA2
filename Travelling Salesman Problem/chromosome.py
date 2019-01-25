class Chromosome:
    def __init__(self, path):
        self.score = 0
        self.path = path
        self.cities_count = []
        self.monster = False

    def __repr__(self):
        return "path = " + str(self.path) + " with: " + str(self.score)

    def comparator(self, b):
        if self.score > b.score:
            return -1
        return 1
