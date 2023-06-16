# Un triplet pythagoréen est un ensemble de 3 entiers naturels a, b, c
# tel que : a < b < c et a² + b² = c²

a, b, c = 0, 0, 0

for c in range(1000):
    for b in range (c): # On veut des nombres a < b < c
        for a in range(b):
            if a**2 + b**2 == c**2:

                if (a + b + c) == 1000:
                    print(a,"+", b, "+",c, "= 1000")
                    print("product of a, b and c is", a*b*c)

