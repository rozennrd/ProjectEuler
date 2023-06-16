"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

# Trois nombres varient :
# - le premier chiffre du dénominateur => c
# - le premier chiffre du numérateur => b
# - le deuxième chiffre, commun aux deux => a
from fractions import Fraction

fractions = []

def verif_egal(frac, n1,n2):
    if frac == n1/n2 and frac < 1:
        print(frac, " = ", n1, "/", n2)
        fractions.append((n1,n2))

for a in range(1,10): #0 n'est pac compris, il ne produit que des fractions triviales
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                frac = int(str(a) + str(b)) / int(str(c)+str(d))
                if a == c :
                    verif_egal(frac, b, d)
                elif a == d:
                    verif_egal(frac, b, c)
                elif b == c:
                    verif_egal(frac, a, d)
                elif b == d:
                    verif_egal(frac, a, c)

result = Fraction(1)
for n1,n2 in fractions:
    result = result * Fraction(n1,n2)
print(result)