import math
from collections import defaultdict
import time

start= time.time()
PRIMES = []
PRIME_DIVISORS = defaultdict(set)


def get_primes_until(n):
    for x in range(2, n+1):
        for d in range(2, int(math.sqrt(x) + 1)):
            if x % d == 0:
                break
        else:
            PRIMES.append(x)
            PRIME_DIVISORS[x].add(x)


def get_prime_divisors(n):
    for p in PRIMES:
        for v in range(1, n//p+1):
            # print(p, v, p*v)
            PRIME_DIVISORS[p * v].add(p)


MAX = 10**2
get_primes_until(MAX)
get_prime_divisors(MAX)
# print(PRIMES)
# print(PRIME_DIVISORS)
RELATIVE_PRIMES = defaultdict(list)

for n in range(1, MAX+1):
    pn = PRIME_DIVISORS[n]

    for nl in range(1, n):
        pnl = PRIME_DIVISORS[nl]
        #print(n, nl, pnl & pn)
        if not (pnl & pn):
            RELATIVE_PRIMES[n].append(nl)
#
# # print(RELATIVE_PRIMES)
N_PHI = {}
for n in RELATIVE_PRIMES:
    if n != 1 :
        N_PHI[n] = n / len(RELATIVE_PRIMES[n])

# import numpy as np
# values = np.array(list(N_PHI.values()))
# print(values.max(), values.argmax()+2)
stop = time.time()
print(stop - start)