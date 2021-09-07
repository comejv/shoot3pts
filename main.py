# Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

import matplotlib.pyplot as plt
import numpy as np

# Paramètres
V0 = float(
    input("Quelle est la vitesse initiale de lancer en mètres par seconde ?"))
T = float(input("Quelle est la hauteur à laquelle le ballon est lancé ?"))

r = 0.24  # Diamètre ballon
g = 9.8  # Accélération gravitationelle en m.s-2
pos_planche = 6.75
D_panier = 0.45
support_panier = 0.15

x_panier = [6.15, 6.6]
h_panier = 3.05 - T  # Hauteur panier relativement au départ du ballon
y_panier = [h_panier, h_panier]


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

# plt.plot(x, centre_inertie, 'r:')
plt.plot(x, centre_inertie, color='red', linewidth=4, linestyle=':')
plt.plot(x_panier, y_panier, marker="x", color="blue", linestyle=":")
plt.ylim(0, 5)
plt.xlim(0, 10)

plt.show()
