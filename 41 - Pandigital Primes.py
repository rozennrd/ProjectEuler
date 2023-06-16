"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations


def is_prime(n):
    """vérifie si un nombre est premier"""
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def get_permutations(n):
    """renvoie l'ensemble des nombres pandigitaux composés de n chiffres, du plus grand au plus petit"""
    perm = []
    for i in permutations(range(1,n)):
        nb = ""
        for digit in i:
            nb += str(digit)
        perm.append(int(nb))
    perm.sort(reverse=True)
    return perm


def get_number():
    """renvoie le plus grand nombre pandigital et premier"""
    for n in range(10,1,-1):
        for i in get_permutations(n):
            if is_prime(i):
                return i


print(get_number())
