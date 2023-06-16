"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
 3/7.
"""

from math import gcd
from fractions import Fraction
from Timer import Timer
from decimal import Decimal


def get_sol(limit):
    dct = {}
    n_sol = 0
    d_sol = 0
    for d in range(1, limit+1):
        n = (3 * d - 1) / 7
        if n % 1 == 0 and n * d > n_sol * d_sol:
            n_sol = int(n)
            d_sol = d
    return n_sol, d_sol


# def get_sol(limit):
#     frac = get_fractions(limit)
#     std = sorted(list(frac))
#     idx = std.index(Fraction(3,7))
#     sol = std[idx-1]
#     return frac[sol]


if __name__ == "__main__" :
    t = Timer()
    t.start()
    print(get_sol(1_000_000))
    t.stop()
    print(t.elapsed)

