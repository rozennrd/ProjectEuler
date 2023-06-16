"""Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e."""


# Calcul de la fraction continue de e à travers une boucle
# on sait que pour chaque boucle, pour une boucle n (n > 0) on a une suite de a valant 1, 2*n, 1
# On veut calculer les chiffres du numérateur pour le 100e convergent de e
# donc est-ce qu'il faut calculer toutes les occurrences et repartir de là à chaque fois ?
# On s'apperçoit que le numérateur au rang i  = numérateur au rang i-1 * fraction +numérateur au rang i-2
# On s'aperçoit aussi d'une sorte de boucle : la fraction continue se répète par série de 3, avec la série au rang
# n = 1, 2*n, 1
# Il faut donc imaginer un autre compteur qui tient compte de combien de boucles ont été imaginées (compteur k)

# Initialisation : les valeurs à l'issue du premier calcul
num1 = 2  # valeur du premier numérateur
num2 = 3  # valeur du deuxième numérateur
frac = 2  # valeur de la fraction continue à la deuxième itération
k = 1 # numéro de la boucle dans laquelle nous sommes (compteur k, tient compte des boucles pour obtenir
# 1,2,1, 1,4,1, 1,6,1, etc)

for i in range (3,101):  # jusqu'à i = 100 puisqu'on veut la somme des chiffres à la 100e itération
    num1, num2 = num2, num1 + num2*frac # on affecte num2 à num1, puis num1 + num2*frac à num2 : c'est le numérateur le plus récent
    if i % 3 == 2 :  # si i modulo 3 vaut 2,il faut augmenter k, et réassigner une nouvelle valeur à la fraction continue
        k+=1
        frac = k*2
    else :
        frac = 1
    print(i, num1, frac, num2)

print(sum([int(n) for n in str(num2)])) # calcul de la somme des chiffres du numérateur