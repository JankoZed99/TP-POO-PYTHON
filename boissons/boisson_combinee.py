from boissons.boisson import Boisson

class BoissonCombinee(Boisson):

    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def cout(self):
        return self.b1.cout() + self.b2.cout()

    def description(self):
        return self.b1.description() + " + " + self.b2.description()
