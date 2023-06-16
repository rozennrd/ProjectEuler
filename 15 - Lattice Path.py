# from itertools import combinations
#
# n = int(input("Combien de cases par rangée sur la grille? "))
# grille = n*n
# choix = ["D" for i in range(n)]
# for i in range(n):
#     choix.append("B")
# print(choix)
#
# count = 1
# for a in combinations(choix, grille):
#     print(a, count)
#     count += 1

# pour traverser la grille, il existe deux choix : Droite, ou Bas ;
# Pour une grille de largeur n, chaque choix doit être emprunté n fois.
# A partir de là, trouver toutes les combinaisons possibles, pour avoir le nombre exact de
# combinaisons.
# Ce sont des statistiques bayésiennes : deux choix pour chaque chemin ; seulement,
# il nous faut le nombre de combinaisons où il y a EXACTEMENT 20 "D" pour 40 items...

"""
Au final : résolu sans Python.
Il s'agit d'analyse combinatoire basique : dans une grille de longueur l, le total du
nombre de choix à faire est t = l * l.
Sur ces t choix, il faut l "Droite" et l "Bas".
La formule pour calculer le nombre de choix à faire est t! / (l!l!) ; ici :
40! / 20!20! = 137846528820
"""