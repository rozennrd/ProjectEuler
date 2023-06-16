# # les nombres triangulaires sont générés par l'addition des nombres naturels.
# # les 10 premiers termes sont : 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
# # 28 est le premier nombre triangulaire qui a plus de 5 diviseurs.
# # quel est le premier nombre triangulaire à avoir plus de 500 diviseurs ?
#
# from functools import reduce
# # générer la liste des nombres triangulaires :
# triangulaires = []
# x=0
# for i in range (1,10000):
#     x = x + i
#     triangulaires.append(x)
# print(triangulaires)
# # premiers=[]
# # for x in range(max(triangulaires)):
# #     for n in premiers :
# #         if n
#
# # def getFactors(n):
# #     factors=[f for f in range(1,n+1) if n%f==0]
# #     return len(factors)
#
# #
# # print(triangulaires)
# # def theTriangulaire(nb):
# #     for n in triangulaires:
# #         if getFactors(n) == nb:
# #             print(n)
# #             break
# #
#
#
# #fonction qui calcule les diviseurs d'un nombre, trouver les premiers nombres
# # qui ont plus de 500 diviseurs
# #établir une liste de nombres premiers
# def primes():
#     nombres_premiers = [2]
#     for i in range(2,max(triangulaires)):
#         test = True
#         for n in nombres_premiers:
#             if i % n == 0:
#                 test = False
#                 break
#         if test:
#             nombres_premiers.append(i)
#     print("le programme a fini de générer les nombres premiers")
#     return nombres_premiers
#
#
# def nb_diviseurs(liste):
#     premiers = primes()
#     for nb in liste:
#         liste_diviseurs = []
#         for i in premiers:
#             while i < nb:
#                 while nb/i == 0:
#                     liste_diviseurs.append(i)
#                     nb=nb/i
#                     if len(liste_diviseurs) == 500:
#                         print("le nombre recherché est %d" % nb)
#                         return nb
#                 else:
#                     print(nb, len(liste_diviseurs))
#                     break
#             pass

#pour trouver les diviseurs d'un nombre, itérer de 1 jusqu'au nombre,
# itérer jusqu'à la racine carrée du nombre - quand on trouve les diviseurs on trouve le quotient

import math
dividers = {}
n = 1
tri = 1

def get_dividers(x):
    root = int(math.sqrt(x))
    div = []

    for n in range(1, root + 1):
        q, r = divmod(x, n)

        if r == 0:
            div.append(n)
            div.append(q)

    div.sort()
    return set(div)

while True:
    div = list(get_dividers(tri))
    div.sort()
    dividers[tri] = div

    if len(div) >= 500:
        print(tri, div, len(div))
        break

    n += 1
    tri += n