from ingredients.decorator import IngredientDecorator

class Sucre(IngredientDecorator):

    def cout(self):
        return self.boisson.cout() + 0.2

    def description(self):
        return self.boisson.description() + ", Sucre"
