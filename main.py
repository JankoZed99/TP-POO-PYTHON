from boissons.cafe import Cafe
from boissons.the import The

from ingredients.lait import Lait
from ingredients.sucre import Sucre

from commande.client import Client
from commande.commande import Commande
from commande.fidelite import Fidelite


client = Client("Ahmed", 1)

cafe = Cafe()
cafe_lait = Lait(cafe)
cafe_lait_sucre = Sucre(cafe_lait)

the = The()

menu = cafe_lait_sucre + the

commande = Commande(client)

commande.ajouter_boisson(menu)

commande.afficher()

fidelite = Fidelite()
fidelite.ajouter_points(client, commande.prix_total())

print("Points fidélité :", client.points_fidelite)
