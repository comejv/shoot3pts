# Author : Côme VINCENT
# Copyrights 2021
# Python 3

# ? Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

import matplotlib.pyplot as plt
import numpy as np

# ! FONCTIONS


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


def touche_arceau():  # Test si distance (centre ballon - arceau) > rayon ballon
    for i in range(len(x)):
        distance_ballon_arceau1 = np.sqrt(
            ((x[i]-x_arceau[0])**2)+((y[i]-y_arceau[0])**2))
        distance_ballon_arceau2 = np.sqrt(
            ((x[i]-x_arceau[1])**2)+((y[i]-y_arceau[1])**2))
        if distance_ballon_arceau1 < r_ballon:
            touche = True
            break
        elif distance_ballon_arceau2 < r_ballon:
            touche = True
            break
        else:
            touche = False
    return touche


# def touche_sol(): # * Pas très utile
#     return (-2*Atan)/(-9.8*(8**-2)*(Acos**-2))
# Paramètres
V0 = float(
    input("Quelle est la vitesse initiale de lancer en mètres par seconde ?"))
# T = float(input("Quelle est la hauteur à laquelle le ballon est lancé ?"))
T = 1.85
A = float(input("Quel est l'angle de lancer en degrés ?"))
Acos, Atan = ACosTan(A)

# Constantes
r_ballon = 0.24  # Diamètre ballon
pos_planche = 6.75  # Distance origine repère - fond terrain
D_panier = 0.45  # Diamètre du panier
x_arceau = [6.15, 6.6]
# Hauteur panier relativement au départ du ballon
y_arceau = [3.05 - T, 3.05 - T]
g = 9.8  # Accélération gravitationelle en m.s-2

# ! MAIN

# Centre inertie ballon
temp_x = np.linspace(0, 10, 60)
y = position(g, V0, Acos, Atan)
# Enlever les valeurs négatives
y = [item for item in y if item >= 0]
# Création array à la bonne taille p/r à y
x = np.linspace(0, temp_x[len(y)], len(y))

# Test si touche le sol et affichage
if touche_arceau() == True:
    resultat = "Le ballon touche l'arceau"
else:
    resultat = "Le ballon ne touche pas l'arceau"


# Affichage courbes
plt.plot(x, y, color='red', linewidth=4,
         linestyle=':', label='Trajectoire du ballon')
plt.plot(x_arceau, y_arceau, marker="x", color="blue",
         linestyle=":", label='Limites du panier')
plt.ylim(0, 4)
plt.xlim(0, 10)

# Affichage infos graph

plt.title(resultat)
plt.legend()

plt.show()
