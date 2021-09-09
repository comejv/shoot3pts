from numpy import sqrt, radians, cos, tan, linspace

def ACosTan(A):

    # Conversion de langle en radians car numpy est en radians
    Arad = radians(A)

    # Création des variables de cos et tan en dehors de l'équation principale pour simplifier la lecture
    Acos = cos(Arad)
    Atan = tan(Arad)

    return Acos, Atan

def position(acceleration_gravitationelle, vitesse_initiale, cosinus_angle, tangeante_angle):
    
    hauteur = -0.5 * acceleration_gravitationelle * (
        (temp_x**2) / ((vitesse_initiale**2) * (cosinus_angle**2))
    ) + tangeante_angle * temp_x

    return hauteur

# Test si distance (centre ballon - arceau) > rayon ballon
def touche_arceau():
    for i in range(len(x)):
        distance_ballon_arceau1 = sqrt(
            ((x[i]-x_arceau[0])**2)+((y[i]-y_arceau[0])**2))
        distance_ballon_arceau2 = sqrt(
            ((x[i]-x_arceau[1])**2)+((y[i]-y_arceau[1])**2))
        print(distance_ballon_arceau1, distance_ballon_arceau2)
        if distance_ballon_arceau1 < r_ballon:
            touche = True
            break
        elif distance_ballon_arceau2 < r_ballon:
            touche = True
            break
        else:
            touche = False
    return touche
