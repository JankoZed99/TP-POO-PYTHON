from commande.commande import Commande

class CommandeSurPlace(Commande):

    def afficher(self):
        print("=== Commande Sur Place ===")
        super().afficher()


class CommandeEmporter(Commande):

    def afficher(self):
        print("=== Commande À Emporter ===")
        super().afficher()
