"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
from functools import reduce
from math import factorial
from Timer import Timer

t1 = Timer()

t1.start()
# def fact(n):
#     return reduce(lambda x,y : x * y, [i for i in range(n+1)])

fact = {i:factorial(i) for i in range(10)}

cache = {}


def fact_equals(n):
    # if n[:-1] in cache :
    #
    sum_fact = reduce(lambda x,y: x+y, [fact[int(dig)] for dig in str(n)])
    return sum_fact == n


def main():
    numbers_ok = [n for n in range(3,10000000) if fact_equals(n)]
    return sum(numbers_ok)


print(main())
t1.stop()
print(t1.elapsed)
