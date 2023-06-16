from itertools import combinations_with_replacement

coins = [200, 100, 50, 20, 10, 5, 2, 1] # valeur des pièces en pence
 # On ne teste pas si 200 pence font 200 pence, pas besoin

#But then we have to count every time any number of coin makes 2 pounds, with a 1£ coin.
#two coins test :
#
#
#
# def changes(amount, coins):
#     ways = [0] * (amount + 1)
#     ways[0] = 1
#     for coin in coins:
#         for j in range(coin, amount + 1):
#             ways[j] += ways[j - coin]
#     return ways[amount]
#
#
# print(changes(200, coins))


# pour chacun des éléments dans la liste : prendre la première pièce, il manque x, générer l'arbre de toutes les combinaisons possibles
# On pourrait faire une fonction récursive avec 8 sous fonctions : chaque sous fonction prendra l'élément à l'indice n et se rappelle
# elle-même et regarde si la valeur qu'elle a maintenant est 200
# solutions = {}
# def branches(choix, sol_courante):
#     somme = sum(sol_courante)
#     if somme == 200:
#         sol_courante.sort()
#         solutions[tuple(sol_courante)] = None
#     else:
#         for c in choix:
#             if somme + c <= 200:
#                 branches(choix, sol_courante + [c])
#
#     return len(solutions)
#
# print(branches(coins, []))

# 200a + 100b + 50c + 20d + 10e + 5f + 2g + 1h = 200


pieces = {200:1, 100:2, 50:4, 20:10, 10:20, 5:40, 2:100, 1:200}
pieces = list(pieces.items())
print(pieces)
solutions = 0

def fonction_calcul(pieces, total_actuel):
    global solutions
    piece_courante, nb_max = pieces[0]
    for n in range(nb_max+1):
        somme = total_actuel + n*piece_courante
        if somme == 200 :
            solutions +=1
        else:
            if len(pieces) >1 and somme < 200:
                fonction_calcul(pieces[1:], somme)

fonction_calcul(pieces, 0)
print(solutions)

