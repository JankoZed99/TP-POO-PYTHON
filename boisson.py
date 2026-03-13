from abc import ABC, abstractmethod

class Boisson(ABC):

    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def __add__(self, other):
        from boissons.boisson_combinee import BoissonCombinee
        return BoissonCombinee(self, other)
