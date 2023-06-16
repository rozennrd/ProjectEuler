"""
It turns out that 12 cm is the smallest length of wire that can be bent to form
 an integer sided right angle triangle in exactly one way, but there are many
 more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000
can exactly one integer sided right angle triangle be formed?


L'idée pour résoudre ceci :
"""
from math import gcd
PRIMES = []
CACHE = {}
FACTORS = {}



"""
formule simplifiée du périmètre à partir du moment où k, m et n respectent
les conditions pour générer des triplets pythagoréens
"""

from collections import defaultdict



def generate_solution(limit):
    SOLUTION = defaultdict(lambda: 0)
    mlimit = int((limit/2)**0.5)
    print (mlimit)
    p = 0
    for m in range(1, mlimit):
        for n in range(1, m):
            # print (SOLUTION)
            # if (m+n)%2 == 1 and gcd(m, n) ==1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            p = a + b + c

            # print(f"{p} = {a} + {b} + {c}")

            SOLUTION[p] += 1

            k=2

    cache = set()
    for k, v in SOLUTION.items():
        it = 1
        while k * it < limit:
            cache.add(k*it)
            it += 1
    for nb in cache :
        if SOLUTION[nb] == 0 :
            SOLUTION[nb] += 1

    s = [k for k, v in SOLUTION.items() if v == 1 and k <= limit]
    print(s)
    print(cache)
    print(SOLUTION)
    return len(s)



print(generate_solution(1_500_000))



# Sol 2

import math

L = 1500000
maxm = int(math.sqrt(L/2))
triple = [0 for x in range(0,L+1)]
ans = 0


for m in range(2,maxm):
    for n in range (1,m):
        if ((m+n)%2)==1 and gcd(m,n)==1:
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            p=a+b+c
            while p<=L:
                triple[p]=triple[p]+1
                if triple[p]==1:
                    ans=ans+1
                if triple[p]==2:
                    ans=ans-1
                p=p+a+b+c
print('ans = ',ans)