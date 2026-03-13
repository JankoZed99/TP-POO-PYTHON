from ingredients.decorator import IngredientDecorator

class Caramel(IngredientDecorator):

    def cout(self):
        return self.boisson.cout() + 0.7

    def description(self):
        return self.boisson.description() + ", Caramel"
