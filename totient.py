import math
from Timer import Timer

t = Timer()
t.start()
PRIMES = []
PRIME_DIVISORS = {}
RELATIVE_PRIMES = {}

def get_primes_until(n):

    for x in range(2, n+1):
        for d in range(2, int(math.sqrt(x) + 1)):
            if x % d == 0:
                break
        else:
            PRIMES.append(x)

MAX = 10**1
get_primes_until(MAX)
# print(PRIMES)

def get_prime_divisors(n):

    if n not in PRIME_DIVISORS:
        s = set()
        for p in PRIMES:
            if p > n:
                break
            elif n % p == 0:
                s.add(p)
        PRIME_DIVISORS[n] = s

    return PRIME_DIVISORS[n]


for n in range(1, MAX+1):
    pn = get_prime_divisors(n)
    RELATIVE_PRIMES[n] = []

    for nl in range(1, n):
        pnl = get_prime_divisors(nl)
        # print(n, nl, pnl & pn)
        if not (pnl & pn):
            RELATIVE_PRIMES[n].append(nl)

# print(PRIME_DIVISORS)
# print(RELATIVE_PRIMES)
N_PHI = {}
for n in RELATIVE_PRIMES:
    if n != 1 :
        N_PHI[n] = n / len(RELATIVE_PRIMES[n])

import numpy as np
values = np.array(list(N_PHI.values()))
print(values.max(), values.argmax()+2)
t.stop()
print(t.elapsed)
# print(values)