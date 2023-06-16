"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?
"""
from math import gcd

from Timer import Timer
from decimal import Decimal

# # Du fait de la range, on ne va pas pouvoir utiliser la méthode avec les
# # nombres premiers...


def get_tot_in_range(n):
    """returns the number of numbers relatively prime to n"""
    tot = 0
    # print(f"*** {n} ***")
    for i in range(int(n/3), int(n/2) +1):
        if 1/3 < i/n < 1/2 and gcd(i, n) == 1:
            tot += 1
    #         print(i)
    # print("***")
    return tot


if __name__ == "__main__":
    t = Timer()
    t.start()
    MAX = 12_001
    s = 0

    for d in range(2, MAX):
        s += get_tot_in_range(d)
        # print(f"d : {d}, s:{s}")
    print(s)
    t.stop()
    print(t.elapsed)