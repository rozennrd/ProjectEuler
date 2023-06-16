"""

"""

from fractions import Fraction
from Timer import Timer

from decimal import *
from math import gcd

# On part de la définition wikipédia, a0 = 1, a1 et a2 et a3 et an = 2
# a0 = 1
# a = 2
# cnt = 0
#
#
# def reduceFraction(x, y):
#     """Function to reduce a fraction to its lowest form"""
#     d = gcd(x, y)
#
#     x = x / d
#     y = y / d
#     print(x, y, d)
#
#     return x, y
#
#
# for i in range (1000):
#     a = Decimal(2 +(1/Decimal(a)))
#     n = Fraction(Decimal(1+(1/a))).limit_denominator()
#
#     # den = n.denominator
#     # num = n.numerator
#     # num, den = reduceFraction(num, den)
#
#     print(n)
#     condition = len(str(n.numerator)) > len(str(n.denominator))
#     print(n.numerator, n.denominator, condition)
#     cnt += condition
# print(cnt)

# n = 1 + (1 / a1)
# print(Fraction(n).limit_denominator(), n)
# a2 = a1+(1/2)
# n2 = 1+ 1/a2
# print(a2, n2)
# a3 = a1+(1/a2)
# n3 = 1+1/a3
# print(a3, n3)
# a4 = a1+1/a3
# n4 = 1+1/a4
# print(a4,n4)

# print(1 + (1/denom))
# print(Fraction(1+(1/denom)).limit_denominator(100))

# Tentative 2
# on part du principe que si une convergente = p/q, la suivante = (p+2q)/(p+q) - on va donc chercher à former
# toutes ces fractions

t = Timer()
t.start()

first_convergent = Fraction(1+1/2)

p = first_convergent.numerator
q = first_convergent.denominator
cnt = 0
for i in range(1000):
    p, q = p + 2 * q,  p + q
    cnt += len(str(p)) > len(str(q))

t.stop()
print (cnt, t.elapsed)
