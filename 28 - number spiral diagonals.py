# générer une spirale de 1001 * 1001 qui soit une spirale de nombres dont le début est au milieu :
import numpy as np

from Timer import Timer
timer1 = Timer()
timer2 = Timer()
timer3 = Timer()

timer1.start()
timer3.start()
a = 1001
spiral = [[0 for i in range (a)]for j in range(a)] # génération de la matrice

n = 1 #initialisation
y = int (a/2) # positions de début ; les positions changeront ppour générer la spirale
x = int(a/2)

spiral[y][x] = n


# on commence à droite, puis on descend de 1, et ensuite on change les valeurs ; à chaque déplacement n += 1.
# définition des mouvements :

def move_right(y, x):
    return y, x+1

def move_down(y,x):
    return y+1, x

def move_left(y,x):
    return y, x-1

def move_up(y,x):
    return y-1, x

def change_value(y,x,n, spiral_):
    """
    Incrémente n et change la valeur dans le tableau à la position (x,y)
    :param y: coordonnées dans la spirale sur l'axe y
    :param x: coordonnées dans la spirale sur l'axe x
    :param n: nombre par lequel remplacer la valeur spiral[y][x]
    :return: None
    """
    n += 1
    spiral_[y][x] = n
    return n


def spiral_values(x, y, n, spiral_):
    N = 1 # nombre de cases de chaque déplacement ; incrémenté de 2 tous les deux déplacements
    while x < a: # tant que la case existe et est remplie (techniquement elle est remplie avec des zéros)
        for i in range(N):
            y, x = move_right(y, x)
            if x==a or y==a:
                return spiral_
            n = change_value(y,x,n, spiral_)
        for j in range(N):
            y, x = move_down(y, x)
            if x==a or y ==a:
                return spiral_
            n = change_value(y, x, n, spiral_)
        N+=1

        for i in range(N):
            y, x = move_left(y, x)
            if x == a or y == a:
                return spiral_
            n = change_value(y,x,n, spiral_)
        for j in range(N):
            y, x = move_up(y, x)
            if x == a or y == a:
                return spiral_
            n = change_value(y, x, n, spiral_)
        N+=1

spiral_values(x, y, n, spiral)
for line in spiral :
    print(line)
timer1.stop()

timer2.start()
# à partir de cette spirale, calculer les sommes des diagonales
diagsum =0
for x in range(len(spiral)):
    diagsum += spiral[x][x]
    xreverse = len(spiral) - 1 - x
    diagsum += spiral[xreverse][x]

print(diagsum-1) # on enlève 1 parce que le centre de la grille (le 1) est compté deux fois dans la somme
timer2.stop()
timer3.stop()

print("génération de la spirale : " , timer1.elapsed)
print("calcul des diagonales : " , timer2.elapsed)
print("temps total : " , timer3.elapsed)

import numpy as np
np_spiral = np.zeros((1001,1001))
npn = 0
y = int (a/2) # positions de début ; les positions changeront ppour générer la spirale
x = int(a/2)
npn = change_value(x, y, npn, np_spiral)
spiral_values(x, y, npn, np_spiral)

diag1 = np.diag(np_spiral).sum()
diag2 = np.diag(np_spiral[::-1]).sum()

print(diag1+diag2 - 1)