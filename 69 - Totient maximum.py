"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n. For
 example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime
 to nine, φ(9)=6.

 It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

 """
from Timer import Timer
from math import gcd
import numpy as np
import pandas as pd


def totient(n):
    """returns the number of numbers relatively prime to n"""
    tot = 0
    # print(f"*** {n} ***")
    for i in range(1, n):
        if gcd(i, n) == 1:
            tot += 1
            # print(i)
    # print("***")
    return(n/tot)



def find_sol(nb):
    """returns the maximum ratio of n/φ(n) for n ≤ nb"""

    # def along_axis(x):
    #     return np.apply(totient, 1, x)
    max_ratio = 0
    max_n = 0

    vf = np.vectorize(totient)
    nbs = np.array(range(2,nb+1))
    tts = vf(nbs)
    # print(f"{nbs=}")
    # print(f"{tts=}")
    nbs2 = pd.DataFrame({"n":nbs, "n/tot(n)":tts})
    # nbs2["n/tot(n)"] = nbs2["n"] / nbs2["totient(n)"]
    # print(nbs2)

    max_nbs = nbs2[nbs2["n/tot(n)"] == nbs2["n/tot(n)"].max()]
    # for n in nbs:
    #
    #
    #     rat = n/totient(n)
    #     if rat > max_ratio:
    #         max_ratio = rat
    #         max_n = nb
    return max_nbs["n"]

#
# def crible_eratosthene(n):
#     prime = [True for i in range(n+1)]
#     p = 2
#     while p*p <= n:
#         if prime[p]:
#             for i in range(p * p, n+1, p):
#                 prime[i] = False
#     return prime
#
# primes={}
# def is_prime(n):
#     if n not in primes:
#         for i in range(n**0.5):
#             if n % i == 0:
#                 primes[n] = False
#                 return False
#         primes[n] = True
#     return primes[n]
#
#         # https://radiusofcircle.blogspot.com/2017/06/project-euler-problem-69-solution-with-python.html
# def get_distinct_prime_factors(n):
#     """returns the number of primes factor of n"""
#     factors = {}
#     cnt = 0
#     div = int(n**0.5)+1
#     for i in range(div, 1, -1):
#         if is_prime(i):
#             if n % i == 0 :
#                 n = n/i
#                 if i not in factors:
#                     factors[i] = None
#                     cnt +=1
#                 if is_prime(n):
#                     if n not in factors:
#                         factors[n] = None
#                         cnt+=1
#     return cnt
#
# def find_result(n):
#     result = 1
#     primes = crible_eratosthene(10)
#     i = 0

"""
OK.Donc pour résoudre ça, on utilise la formule d'Euler : 
tot(n) = n * (produit (1 - 1/pk) pour i allant de 1 à k)
p1, p2, p... pk étant les facteurs premiers de n. 

Nous allons donc avoir besoin de : 
* générer les nombres premiers
* trouver les facteurs premiers de n
* générer la fonction qui donne le résultat n/tot(n), soit simplement 
(produit (1 - 1/pk) pour i allant de 1 à k)
* trouver le n/tot(n) maximum et le n associé pour n <= 1_000_000

"""
from math import sqrt

PRIMES = []
CACHE = {}
def is_prime(n):
    """Vérifie qu'un nombre est premier"""
    if n in CACHE:
        return True
    if n <= 1 or n % 1 != 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    CACHE[n]=None
    return True


def prime_generator(limit):
    """
    Génère une liste de nombre premiers sous un certain seuil (limite).
    Ne retourne rien, utilise la liste globale PRIMES
    """
    for i in range(limit):
        if is_prime(i):
            PRIMES.append(i)



def get_prime_factors(n):
    """returns the number of primes factor of n"""
    factors = {}
    i = 0
    if not is_prime(n):
        while PRIMES[i] < n :
            while n % PRIMES[i] == 0:
                if PRIMES[i] not in factors:
                    factors[PRIMES[i]] = None
                n = n / PRIMES[i]
                if is_prime(n):
                    if n not in factors:
                        factors[n] = None
                    return factors.keys()
            i += 1
    return factors.keys()



def get_ratio_tot_(n):
    factors = get_prime_factors(n)
    prod = 1
    for n in factors:
        prod *= 1 - 1 / n
    return 1/ prod


if __name__ == "__main__":
    t = Timer()
    t.start()
    #print(find_sol(10000))
    MAX = 1_000_000
    max_ratio = 0
    max_n = 0
    prime_generator(int(MAX**0.5)+1)
    for i in range(MAX):
        r = get_ratio_tot_(i)
        if r >max_ratio:
            max_ratio = r
            max_n = i
    print (max_n)
    t.stop()
    print(t.elapsed)