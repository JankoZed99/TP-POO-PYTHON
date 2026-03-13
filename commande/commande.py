class Commande:

    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher(self):
        print("Commande du client :", self.client.nom)

        for b in self.boissons:
            print("-", b.description())

        print("Prix total :", self.prix_total(), "€")
