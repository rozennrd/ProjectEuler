"""
The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?
"""

from Timer import Timer
from math import factorial


def calc_next_fact_in_chain(n):
    s = 0
    for digit in str(n):
        s += factorial(int(digit))
    return s


def calc_len_chain(n):
    nxt = n
    nbs = {nxt: None}
    while True:
        nxt = calc_next_fact_in_chain(nxt)
        if nxt in nbs:
            return len(nbs)
        nbs[nxt] = None
        # print(n, nbs)


if __name__ == "__main__":
    t = Timer()
    t.start()
    MAX = 1_000_000
    s = 0
    for i in range (1, MAX):
        if calc_len_chain(i) == 60:
            s+=1

    print(s)
    t.stop()
    print(t.elapsed)

    print("** SOLUTION 2 **")
    t.reset()
    t.start()

    fac = lambda n: 1 if n <= 1 else n * fac(n - 1)
    digifac = {str(n): fac(n) for n in range(0, 10)}
    sum_fac_digits = lambda n: sum(digifac[d] for d in str(n))


    def chainsize(start):
        n = start
        cache = set()
        while (n := sum_fac_digits(n)) not in cache:
            cache.add(n)
        return len(cache) + 1


    def count_chains_of(N):
        return sum(1 for n in range(1, 1000000) if chainsize(n) == N)
    print(count_chains_of(60))
    t.stop()
    print(t.elapsed)