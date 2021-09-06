# Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

import matplotlib.pyplot as plt
import numpy as np

V0 = 10
g = 9.8
A = 45

A = np.radians(A)  # Problème : l'équation est en degrés !

print(A) # La conversion en radians semble être OK

x = np.linspace(0, 15, 60)

#ERREUR AU NIVEAU DU CALCUL DE COS
y = -0.5 * g * (
    (x**2) / ((V0**2) * (np.degrees(np.cos(A))**2))
    ) + np.degrees(np.tan(A)) * x

plt.plot(x, y) 

plt.show()
