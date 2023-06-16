"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Square 	  	P4,n=n2 	  	1, 4, 9, 16, 25, ...
Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
Octagonal 	  	P8,n=n(3n−2) 	  	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281,  has three interesting properties.

    The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including
    the last number with the first).
    Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a
    different number in the set.
    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square,
pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""
from itertools import permutations


NB_LISTES = 3  # taille de la liste de nombres finale = nombre de fonctions vérifiées

def triangle(n):
    return n * (n + 1) / 2


def square(n):
    return n ** 2


def pentagonal(n):
    return n * (3 * n - 1) / 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) / 2


def octagonal(n):
    return n * (3 * n - 2)


# First thing to do is define limits for each kind of numbers : we want 4 digits numbers - let's define sets for all
# kinds of numbers
def four_dig_nb(function):
    lst = []
    n = 1
    while len(str(int(function(n)))) < 5:
        n += 1
        if len(str(int(function(n)))) == 4:
            lst.append(int(function(n)))
    return lst


# Then we need to generate lists of numbers of each kind
triangle_nb = four_dig_nb(triangle)
square_nb = four_dig_nb(square)
pent_nb = four_dig_nb(pentagonal)
hex_nb = four_dig_nb(hexagonal)
hept_nb = four_dig_nb(heptagonal)
oct_nb = four_dig_nb(octagonal)

lists = [square_nb, pent_nb, hex_nb, hept_nb, oct_nb]
lists_order_to_check = permutations(lists[:NB_LISTES-1])

# Then, we will need to assess if the end of the numbers of one kind is the same as numbers of one other kind ; if
# numbers are the same as another in the set, break.


# It's a problem of lists ordering : we need to check every list order to know
# so, we need to generate every list order

# print(triangle_nb)
# for l in lists[0:NB_LISTES-1]:
#     print(l)
#
#
# for liste_group in lists_order_to_check:
#     for liste in liste_group:
#         print(liste)



#
# def end_is_begining(n, l):
#     """générateur de tous les nombres commençant par la fin de n dans la liste l """
#     str_n = str(n)
#     for nb in l:
#         if str_n[2:4] == str(nb)[0:2]:
#             yield nb
#
#
# def check_nb(l, n, i, ordered_lists):
#     """Fonction récursive permettant de vérifier si un nombre de la liste suivante dans lists correspond au
#     début de cette liste
#     Problème : toutes les listes ne sont pas générées ! Seule la première est générée à chaque fois
#     """
#
#     print(l, i)
#     if i == NB_LISTES-1:
#         return l
#     else:
#         nbs = end_is_begining(n, ordered_lists[i])
#         if nbs is None:
#             return None
#         else:
#             for nb in nbs :
#                 end_is_begining(nb, ordered_lists[i])
#                 l.append(nb)
#                 check_nb(l, nb, i + 1, ordered_lists)
#
#
# def check_nb_possibilities(n, liste):
#     for nb in liste:
#         pass
#
# def check_paths(n, lists):
#     pass

#
# if __name__ == "__main__":
#     possible_paths = []
#     for ordered_lists in lists_order_to_check:
#         print(ordered_lists)
#         for n in triangle_nb:  # Pour chaque nombre dans la liste de nombres triangulaires
#             l = [n]  # une liste l est créée, avec ce nombre à l'intérieur
#             check_nb(l, n, 0, ordered_lists)
#             if len(l) == NB_LISTES:
#                 if str(l[0])[2:4] == str(l[-1])[0:2]:
#                     print(l)
#                     print(sum(l))
#                     break
#

# Pas la bonne approche visiblement : est-ce que "ordered set" ça veut dire set avec les nombres dans l'ordre ? OUI
# Plutôt que les fonctions dans l'ordre ? Et dans ce cas, un nombre de chaque type, chacun étant plus grand que le
# précédent  + commençant par les mêmes nombres !
# TODO: les différents ordres de liste sont désormais explorés, mais ne renvoient pas le bon résultat - à explorer -
#  renvoie 0 où devrait renvoyer d'autres nombres




## test 2 :
#

def end_is_beg(n1, n2):
    if str(n1)[2:] == str(n2)[:2]:
        return True
    return False


def sols_in_list(n, l):
    sols = []
    for nb in l:
        if end_is_beg(nb, n):
            sols.append(nb)
    return sols
#
#
# # meilleure idée mais à retravailler, ne marche pas
#
#
# for ll in list(lists_order_to_check) :  # pour chaque ordre de listes (sq-pen-hex-hep-oct, sq-hex-oct-hep-pen ...)
#     solutions = [0 for i in range(NB_LISTES)]
#     for n in triangle_nb:  # on prend chaque nombre pouvant débuter la chaîne
#         solutions[0] = n
#         for i in range(len(ll)): # on prend chaque liste du groupe de listes
#             l = ll
#
#             for nb in l:# on rprend chaque
#                 if str(nb)[0:2] == str(solutions[i])[2:]:
#                     if i == NB_LISTES-2:
#                         if str(nb)[2:] == str(n)[0:2]:
#                             print(sum(solutions))
#                     else :
#                         solutions[i+1] = nb
#
#             print(solutions)




for nbs in triangle_nb: # pour chaque nombre de triangle_nb (donc pour chaque nombre triangulaire) on prend le nombre
    solutions = [nbs]  # on l'ajoute à la listes de solutions
    i = 0
    for ll in list(lists_order_to_check):
        # Puis, pour chaque liste à examiner :
        for l in ll:
            sols = []
            # on vérifie chaque nombre,
         # et on ajoute à solutions dans une nouvelle liste (liste de niveau 2, 3, n) tous les
        # nombres correspondant à une solution possible compatible avec nb
            # puis on prend chaque nombre dans la liste n2, qu'on vérifie avec la liste n3 (liste suivante
        # si ce nombre a au moins une solution dans n2:
            #on le garde
        # sinon
            # on l'enlève


# a essayer : tirer 6 parmi l'ensemble de tous les nombres et vérifier si chaque catégorie est représentée dans la
# liste, et si c'est cyclique



