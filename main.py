# Le but est de trouver les vecteurs V et A pour que le ballon lancé rentre dans le panier sans toucher l'arceau

import matplotlib.pyplot as plt
import numpy as np

V0 = 10
g = 9.8
A = 45

Arad = np.radians(A)  # Problème : l'équation est en degrés !

print(A) # La conversion en radians semble être OK

Acos = np.cos(Arad)

Atan = np.tan(Arad)

x = np.linspace(0, 15, 30)

y = -0.5 * g * (
    (x**2) / ((V0**2) * (Acos**2))
    ) + Atan * x

plt.plot(x, y) 

plt.show()
