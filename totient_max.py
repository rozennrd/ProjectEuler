from Timer import Timer

PRIMES = []
CACHE = {}
def is_prime(n):
    """Vérifie qu'un nombre est premier en utilisant le cache"""
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
    MAX = 1_000_000
    max_ratio = 0
    max_n = 0
    prime_generator(int(MAX**0.5)+1)
    for i in range(MAX):
        r = get_ratio_tot_(i)
        if r > max_ratio:
            max_ratio = r
            max_n = i
    print (max_n)
    t.stop()
    print(t.elapsed)
