"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so
 φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.
"""
from Timer import Timer
from decimal import Decimal

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


def get_tot(n):
    if is_prime(n):
        return n-1
    factors = get_prime_factors(n)
    prod = Decimal(1)
    for nb in factors:
        prod *= Decimal(1 - 1 / nb)
    return round(Decimal(n*prod))


def get_ratio_tot_(n):
    factors = get_prime_factors(n)
    prod = 1
    for nb in factors:
        prod *= Decimal(1 - 1 / nb)
    return Decimal(1/ prod)




if __name__ == "__main__":
    t = Timer()
    t.start()

    MAX = 10_000_000
    min_ratio = 100000
    n =0
    prime_generator(int(MAX**0.5)+1)

    for i in range(2, MAX):
        tt = get_tot(i)
        if sorted(str(int(tt))) == sorted(str(i)):
            r = i / tt
            print(f"n = {i}, tot(n) = {tt}, n/tot(n) = {r}")
            if r < min_ratio:
                min_ratio = r
                n = i
    print (n, min_ratio)
    t.stop()
    print(t.elapsed)
