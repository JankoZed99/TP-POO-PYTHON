from boissons.boisson import Boisson

class IngredientDecorator(Boisson):

    def __init__(self, boisson):
        self.boisson = boisson
