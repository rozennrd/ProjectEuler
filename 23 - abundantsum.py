# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:59:12 2021

@author: rrenaud
"""

# ProjectEuler Problem 23 : non-abundant sums
cache = {}


def diviseurs(n):
    if n not in cache :
        t = []
        for i in range(1, int(n**0.5) +1):
            q,r = divmod(n,i)
            if r == 0:
                t.append(i)
                t.append(q)
        cache[n] = sorted(t)
    return cache[n]

cache2 = {}


def abundant(n):
    if n not in cache2:
        cache2[n] = sum(diviseurs(n)[:-1]) > n
    return cache2[n]

    
def sumofabundant(n):
    for i in range (1, n+1):
        if abundant(i) and abundant(n-i) :
            return True
    return False


def nonabundantsum():
    s = 0
    for i in range(1, 28123 +1):
        if sumofabundant(i) == False:
            s += i
    return s


print(nonabundantsum())
# Devrait retourner 4179871, retourne 4179595...