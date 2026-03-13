class Fidelite:

    def ajouter_points(self, client, montant):
        points = int(montant)
        client.points_fidelite += points


class CommandeFidele(Fidelite):

    def valider(self, commande):
        total = commande.prix_total()
        self.ajouter_points(commande.client, total)
