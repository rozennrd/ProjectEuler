import math
from collections import defaultdict
import time

start= time.time()
PRIMES = []
PRIME_DIVISORS = defaultdict(set)
PRIME_DIVISORS_MULTIPLES = defaultdict(list)
DIVISORS = defaultdict(set)


def get_primes_until(n):
    for x in range(2, n+1):
        for d in range(2, int(math.sqrt(x) + 1)):
            if x % d == 0:
                break
        else:
            PRIMES.append(x)
            PRIME_DIVISORS[x].add(x)


def get_prime_divisors_until(n):
    for p in PRIMES:
        for v in range(1, n//p+1):
            # print(p, v, p*v)
            PRIME_DIVISORS[p * v].add(p)


def get_divisors_until(n):
    for x in range(n):
        for d in range(2, int(math.sqrt(x)) + 1):
            q , r = divmod(x, d)
            if r == 0:
                DIVISORS[x].add(q)
                DIVISORS[x].add(d)


def get_prime_divisors_multiples_until(n):
    for p in PRIMES:
        for v in range(1, n//p+1):
            # print(p, v, p*v)
            PRIME_DIVISORS_MULTIPLES[p * v] += [x*p for x in range(1, v)]


MAX = 10**2
get_primes_until(MAX)
get_prime_divisors_multiples_until(MAX)


# print(PRIMES)
# print(PRIME_DIVISORS_MULTIPLES)
RELATIVE_PRIMES = {}
# #
for n in range(1, MAX+1):
    mdn = set(PRIME_DIVISORS_MULTIPLES[n])
    upton = set(range(1, n))
    RELATIVE_PRIMES[n] = mdn ^ upton

# #
# print(RELATIVE_PRIMES)
N_PHI = {}
for n in RELATIVE_PRIMES:
    if n != 1 :
        N_PHI[n] = n / len(RELATIVE_PRIMES[n])
#
import numpy as np
values = np.array(list(N_PHI.values()))
print(values.max(), values.argmax()+2)
# print(RELATIVE_PRIMES)
stop = time.time()
print(stop - start)