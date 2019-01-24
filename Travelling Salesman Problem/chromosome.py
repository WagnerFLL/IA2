class Chromosome:
    def __init__(self, path):
        self.score = 0
        self.path = path
        self.cities_count = []

    def __repr__(self):
        return "path = " + str(self.path) + " with: " + str(self.score)
