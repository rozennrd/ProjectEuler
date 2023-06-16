# """
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# """
from Timer import Timer
t = Timer()

t.start()
# #
# primes = []
# cache = {}
#
#
# def is_prime(n):
#     if n in cache:
#         return True
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     cache[n]=None
#     return True
#
#
# limit = 1000
# #
# # def consecutive_prime_generator():
# #     for i in range(2, 1000000):
# #         is_prime(i)
# #
# # consecutive_prime_generator()
# #
# # # https://www.mikescher.com/blog/1/Project_Euler_with_Befunge/problem-050
# #
# # somme=0
# # i = 0
# # while somme < 1000000:
# #     somme += primes[i]
# #     i += 1
# # print(i-1)
# #
# # t.stop()
# # print(t.elapsed)
#
#
# # D'abord, générer tous les nombres premiers sous un million
#
# def prime_generator():
#     for i in range(limit):
#         if is_prime(i):
#             primes.append(i)
#
# prime_generator()
# print("génération nombres premiers ok")
# # Calculer la chaine maximale ayant une somme sous 1 000 000
# # print("Calcul de la chaîne ayant une longueur maximale")
# # somme = 0
# # for n in range(len(primes)):
# #     somme += primes[n]
# #     if somme > 1000000:
# #         print(somme)
# #         print(n)
# #         print(n-1)
# #         break
# # Ce calcul nous a donné une chaîne maximale de 547 nombres premiers
# # Nous ne le referons pas, il est donc commenté.
#
# # On crée un scanner qui se déplace d'abord de droite à gauche puis de gauche à droite, en diminuant sa taille à chaque fois
# somme = 0
# i = 0
#
#
# # initialisation de la somme ; en théorie, la somme des 547 nombres premiers
#
# print("avant initialisation de la somme")
# while somme < limit:
#     somme += primes[i]
#     i +=1
#
#
# print("somme initialisée correctement. Vaut ", somme)
# # initialisation du scanner :
# j = 0 # indice du nombre le plus à gauche
# somme_is_prime = False
# while not somme_is_prime:
#     # gauche à droite :
#     while somme < limit:
#         somme += primes[i] # addition du nombre le plus à droite
#         somme -= primes[j] # retrait du nombre le plus à gauche
#
#         if somme < limit:
#             i += 1 #incrémentation des compteurs
#             j += 1
#         somme_is_prime = is_prime(somme) and somme < limit
#         if somme_is_prime:
#             break
#     if somme_is_prime:
#         break
#     # réduction du scanner
#     print("sortie de la boucle numéro 1")
#     print("Somme actuelle : ", somme, ". Limite basse : ", j, ". Limite haute : ", i)
#
#     somme -= primes[j]
#     j += 1
#     # déplacement de droite à gauche
#
#     while j > 0:
#         if j > 0:
#             i -= 1
#             j -= 1
#         print("Nous sommes dans la boucle numéro 2")
#         somme -= primes[i]
#         somme += primes[j]
#
#         somme_is_prime = is_prime(somme)
#         if somme_is_prime:
#             break
#     if somme_is_prime:
#         break
#     print("Somme actuelle : ", somme, ". Limite basse : ", j, ". Limite haute : ", i)
#     # réduction du scanner
#     somme -= primes[i]
#     i -= 1
#
# print(somme)
#


##########################
# Tentative n° 2
##########################

# On génère une liste de nombres premiers

# On génère un scanner
# > Définir une borne de début et une borne de fin
# > Définir l'écart maximal entre la borne de début et la borne de fin (= la plus longue suite de nombres premiers
#     pour arriver à la limite. -> c'est en partant du premier nombre, le plus petit, qu'on la trouve
#     (borne de début = 0)
# > Réduire la longueur du scanner de 1, et commencer à le déplacer de droite à gauche :
#    >> incrémentation des deux bornes (début et fin) pour conserver le même écart
#    >> La somme perd le nombre le plus à gauche et gagne un nombre plus à droite
#    >> Arrêt de la procédure si somme > limite
# > Réduire la longueur du scanner de 1 et repartir dans l'autre sens :
#    >> décrémentation des deux bornes (début et fin) pour conserver le même écart
#    >> La somme gagne le nombre le plus à gauche et perd le nombre le plus à droite
#    >> Arrêt de la procédure si on ne peut pas aller plus loin, c'est à dire si la borne de début = le premier nombre.
# > Répéter la procédure jusqu'à ce que la somme de nombre consécutifs soit première
# > afficher la somme



primes = []
cache = {}
limit = 1000000 # initialisation de la limite

def is_prime(n):
    """Vérifie qu'un nombre est premier"""
    if n in cache:
        return True
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    cache[n]=None
    return True


def prime_generator():
    """génère une liste de nombre premiers sous un certain seuil (limite). Ne retourne rien"""
    for i in range(limit):
        if is_prime(i):
            primes.append(i)

prime_generator()
print("génération nombres premiers ok")


def max_length_sum(limit):
    """Définit la longueur de la plus grande chaîne de nombres premiers"""
    somme = 0
    i = 0
    while somme < limit:
        somme += primes[i]
        i+=1
    i -= 1
    somme -= primes[i]
    return somme, i


def find_biggest_prime_nb(limit):
    deb = 1

    somme_nb, fin = max_length_sum(limit)

    while deb < fin:
        # Condition d'arrêt : si la borne de début est supérieure à la borne de fin, ça voudra dire qu'on a loupé
        # quelque chose. Pas besoin de tourner plus.

        # Puis on repart dans l'autre sens, de gauche à droite :
        while sum(primes[deb:fin]) < limit:
            deb += 1
            fin += 1
            somme_nb = sum(primes[deb:fin])
            if is_prime(somme_nb) and somme_nb < limit:  # Vraiment à chaque étape
                return somme_nb

        # Puis on réduit encore le scanner, à gauche cette fois
        deb += 1  # on ajoute 1 à la borne de début pour réduire l'écart avec la borne de fin
        somme_nb = sum(primes[deb:fin])
        if is_prime(somme_nb) and somme_nb < limit:  # On vérifie une dernière fois
            return somme_nb

        # Droite à gauche : la somme perd le nombre le plus à droite et gagne le plus à gauche
        while deb > 0:
            deb -= 1
            fin -= 1
            somme_nb = sum(primes[deb:fin])
            if is_prime(somme_nb) and somme_nb < limit:
                return somme_nb
        # ici deb = 0, donc on réduit d'abord le scanner. On perd le nombre le plus à droite, puisqu'en théorie c'est là
        # qu'il reste des nombres à regarder.

        fin -= 1
        somme_nb = sum(primes[deb:fin])
        if is_prime(somme_nb) and somme_nb < limit:  # on vérifie vraiment à toutes les étapes : on ne veut louper aucun nb
            return somme_nb


        # Puis on enchaîne jusqu'à trouver la bonne réponse ! ici s'arrête la fonction que nous allons tester de ce pas.



print(find_biggest_prime_nb(limit))
t.stop()
print(t.elapsed)