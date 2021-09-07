# Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

import matplotlib.pyplot as plt
import numpy as np

V0 = float(
    input("Quelle est la vitesse initiale de lancer en mètres par seconde ?"))
g = 9.8  # Accélération gravitationelle en m.s-2
T = float(input("Quelle est la hauteur à laquelle le ballon est lancé ?"))
H_panier = 3.05 - T  # Hauteur panier relativement au départ du ballon
r = 0.24  # Diamètre ballon

pos_planche = 6.75
D_panier = 0.45
support_panier = 0.15
# pos_panier1 = [pos_planche-support_panier-D_panier,H_panier]
# pos_panier2 = [pos_planche-support_panier,H_panier]

x_panier = [6.15, 6.6]
y_panier = [3.05,3.05]

def ACosTan(A):

    # Conversion de langle en radians car numpy est en radians
    Arad = np.radians(A)

    # Création des variables de cos et tan en dehors de l'équation principale pour simplifier la lecture
    Acos = np.cos(Arad)
    Atan = np.tan(Arad)

    return Acos, Atan


x = np.linspace(0, 10, 30)


def position(acceleration_gravitationelle, vitesse_initiale, cosinus_angle, tangeante_angle):
    hauteur = -0.5 * acceleration_gravitationelle * (
        (x**2) / ((vitesse_initiale**2) * (cosinus_angle**2))
    ) + tangeante_angle * x

    return hauteur


Acos, Atan = ACosTan(float(input("Quel est l'angle de lancer en degrés ?")))

centre_inertie = position(g, V0, Acos, Atan)

# Problème : il faut ajouter le rayon perpendiculèrement au centre d'inertie
haut_ballon = position(g, V0, Acos, Atan) + (r/2)

plt.plot(x, centre_inertie, x, haut_ballon)
plt.scatter(x_panier, y_panier, shape='x') # Erreur ici pour afficher des points
plt.ylim(0,5)
plt.xlim(0,10)

plt.show()
