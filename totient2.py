import math
import fractions
from Timer import Timer

t = Timer()
t.start()

RELATIVE_PRIMES = {}
MAX = 10 ** 1

for n in range(2, MAX+1):
    RELATIVE_PRIMES[n] = []

    for nl in range(1, n):
        f = fractions.Fraction(nl, n)
        if f.numerator == nl:
            RELATIVE_PRIMES[n].append(nl)

# print(RELATIVE_PRIMES)

N_PHI = {}
for n in RELATIVE_PRIMES:
    N_PHI[n] = n / len(RELATIVE_PRIMES[n])

import numpy as np
values = np.array(list(N_PHI.values()))
print(values.max(), values.argmax()+2)
t.stop()
print(t.elapsed)
# print(values)