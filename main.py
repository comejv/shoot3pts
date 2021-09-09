# Author : Côme VINCENT
# Copyrights 2021
# Python 3.6

# ? Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

# -> Trouver un moyen de modéliser volume ballon. Peut-être juste au moment de passer l'arceau ?

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


def touche_sol():
    return (-2*Atan)/(-9.8*(8**-2)*(Acos**-2))


# Paramètres
V0 = float(
    input("Quelle est la vitesse initiale de lancer en mètres par seconde ?"))
T = float(input("Quelle est la hauteur à laquelle le ballon est lancé ?"))
A = float(input("Quel est l'angle de lancer en degrés ?"))
Acos, Atan = ACosTan(A)

# Constantes
r_ballon = 0.24  # Diamètre ballon
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


# Affichage courbes
plt.plot(x, y, color='red', linewidth=4,
         linestyle=':', label='Trajectoire du ballon')
plt.plot(x_arceau, y_arceau, marker="x", color="blue",
         linestyle=":", label='Limites du panier')
plt.ylim(0, 4)
plt.xlim(0, 10)

# Affichage infos graph
plt.legend()

plt.show()
