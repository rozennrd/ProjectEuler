"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt
from Timer import Timer
t = Timer()
t.start()

primes = [2]


def is_prime(n):
    if n in primes:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    primes.append(n)
    return True


def check_goldbach_is_wrong(n):
    for prime in primes:
        if prime < n :
            if sqrt((n - prime) / 2) % 1 == 0:
                return False
    return True



def main():
    nb = 3
    while True :
        if is_prime(nb):
            pass
        elif check_goldbach_is_wrong(nb):
            return nb
        nb+=2


print(main())
t.stop()
print(t.elapsed)