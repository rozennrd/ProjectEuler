"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for
 d ≤ 1,000,000?
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

if __name__ == "__main__":
    t = Timer()
    t.start()
    MAX = 1_000_001
    s = 0
    prime_generator(int(MAX ** 0.5) + 1)

    for d in range(2, MAX):
        s += get_tot(d)
        # print(f"d : {d}, s:{s}")
    print(s)
    t.stop()
    print(t.elapsed)