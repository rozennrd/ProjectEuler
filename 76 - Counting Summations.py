"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""
from collections import defaultdict


def fonction_calcul(pieces, total_actuel):
    global solutions
    piece_courante, nb_max = pieces[0]
    for n in range(nb_max + 1):
        somme = total_actuel + n * piece_courante
        if somme == 100:
            solutions += 1
        else:
            if len(pieces) > 1 and somme < 200:
                fonction_calcul(pieces[1:], somme)



def get_sol(n):
    nbs = {i : n//i for i in range(1, n) }
    nb = list(nbs.items())
    print(nbs)
    solutions = 0

    fonction_calcul(nb, n)
    print(solutions)

# get_sol(5)


# def makechange(howmuch, coins):
#     if len(coins) == 1: return howmuch % coins[0] and 0 or 1
#     return sum(makechange(newtotal, coins[1:]) for newtotal in range(howmuch, -1, -coins[0]))
# print (makechange(100, [x for x in range(100,0,-1)]))
nbs = [ i for i in range(101) ]
amount = 100

memo = [[0 for i in range(amount+1)] for j in range(amount+1)]

def ways(tg, avc):
    if avc <= 1:
        return 1
    t = tg
    if memo [t][avc] > 0 : return memo[t][avc]
    res = 0
    while tg >= 0:
        res = res +ways(tg, avc-1)
        tg = tg  - nbs[avc]
    memo[t][avc]=res
    return res

print(ways(amount, amount))
for line in memo :
    print(line)


# réponse attendue 100 can be generated in 190569291 ways
# Solution took 0,0092 ms