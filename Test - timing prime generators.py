from Timer import Timer

t = Timer()
t.start()

primes = []
cache = {}
def is_prime(n):
    """Vérifie qu'un nombre est premier"""
    if n in cache:
        return True
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    cache[n]=None
    return True


def prime_generator(limit):
    """génère une liste de nombre premiers sous un certain seuil (limite). Ne retourne rien"""
    for i in range(limit):
        if is_prime(i):
            primes.append(i)

print(prime_generator(1000))
t.stop()
print("Solution 1 : ", t.elapsed)

t.reset()
t.start()
def erathostene(n):
    """génère une lsite contenant les nombres premiers jusqu'à n"""
    is_prime = [True for i in range(n+1)]
    for i in range(n+1):
        if is_prime[i]:
            j = 2
            while i*j <= n:
                is_prime[i*j] = False
                j += 1

    return [i for i in range(n+1) if is_prime[n]]

print(erathostene(1000))
t.stop()
print("Solution 2 : ", t.elapsed)