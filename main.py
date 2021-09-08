# Author : Côme VINCENT
# Copyrights 2021
# Python 3.6
# ? Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau
import matplotlib.pyplot as plt
import numpy as np

# Fonctions


def ACosTan(A):

    # Conversion de langle en radians car numpy est en radians
    Arad = np.radians(A)

    # Création des variables de cos et tan en dehors de l'équation principale pour simplifier la lecture
    Acos = np.cos(Arad)
    Atan = np.tan(Arad)

    return Acos, Atan


def position(acceleration_gravitationelle, vitesse_initiale, cosinus_angle, tangeante_angle):
    hauteur = -0.5 * acceleration_gravitationelle * (
        (temp_x**2) / ((vitesse_initiale**2) * (cosinus_angle**2))
    ) + tangeante_angle * temp_x

    return hauteur


# Paramètres
V0 = float(
    input("Quelle est la vitesse initiale de lancer en mètres par seconde ?"))
T = float(input("Quelle est la hauteur à laquelle le ballon est lancé ?"))
Acos, Atan = ACosTan(float(input("Quel est l'angle de lancer en degrés ?")))

# Constantes
r = 0.24  # Diamètre ballon
pos_planche = 6.75  # Distance origine repère - fond terrain
D_panier = 0.45  # Diamètre du panier
x_arceau = [6.15, 6.6]
h_arceau = 3.05 - T  # Hauteur panier relativement au départ du ballon
y_arceau = [h_arceau, h_arceau]
g = 9.8  # Accélération gravitationelle en m.s-2

# Centre inertie ballon
temp_x = np.linspace(0, 10, 60)
y = position(g, V0, Acos, Atan)
# Enlever les valeurs négatives
y = [item for item in y if item >= 0]
# Création array à la bonne taille p/r à y
x = np.linspace(0, temp_x[len(y)], len(y))

# ! L'équation ne marche, pas, elle retourne les mêmes valeurs que y
# Bas ballon
y2 = position(g, V0, Acos, Atan)
# Enlever les valeurs négatives
y2 = [item for item in y if item >= 0]
# Création array à la bonne taille p/r à y
x2 = np.linspace(0, temp_x[len(y2)], len(y2))

# Affichage courbes
plt.plot(x, y, color='red', linewidth=4, linestyle=':')
plt.plot(x2, y2, color='blue', linewidth=1, linestyle='-')
plt.plot(x_arceau, y_arceau, marker="x", color="blue", linestyle=":")
plt.ylim(0, 5)
plt.xlim(0, 10)

plt.show()
