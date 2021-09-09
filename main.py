# Author : Côme VINCENT
# Copyrights 2021
# Python 3.6

# ? Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

import matplotlib.pyplot as plt
from numpy import linspace
from fonctions import ACosTan, position, touche_arceau, temp_x


# * Pas très utile


def touche_sol():
    return (-2*Atan)/(-9.8*(8**-2)*(Acos**-2))


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
temp_x = linspace(0, 10, 60)
y = position(g, V0, Acos, Atan)
# Enlever les valeurs négatives
y = [item for item in y if item >= 0]
# Création array à la bonne taille p/r à y
x = linspace(0, temp_x[len(y)], len(y))

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
