"""
CONTEXTE :
Diophantine equation, equation involving only sums, products, and powers in
which all the constants are integers and the
 only solutions of interest are integers. For example, 3x + 7y = 1 or
 x2 − y2 = z3, where x, y, and z are integers.
 Named in honour of the 3rd-century Greek mathematician Diophantus of
 Alexandria, these equations were first
 systematically solved by Hindu mathematicians beginning with Aryabhata
 (c. 476–550).

 Pell Equations

    Main article: Pell equation

A Pell equation is a type of Diophantine equation in the form x^2-Dy^2= +/-1
for natural number D.
The solutions to the Pell equation when D is not a perfect square are connected
 to the continued fraction expansion
of sqrt(D). If a is the period of the continued fraction and C_k=P_k/Q_k is the
 kth convergent, all solutions
to the Pell equation are in the form (P_{ia},Q_{ia}) for positive integer i.
https://artofproblemsolving.com/wiki/index.php/Pell_equation
https://brilliant.org/wiki/quadratic-diophantine-equations-pells-equation/


PROBLEME :
Consider quadratic Diophantine equations of the form:
        x**2 – D * y**2 = 1
For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers when D is
square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:
        3**2 – 2×2**2 = 1
        2**2 – 3×1**2 = 1
        9**2 – 5×4**2 = 1
        5**2 – 6×2**2 = 1
        8**2 – 7×3**2 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest
value of x is obtained.

https://codegolf.stackexchange.com/questions/183298/fundamental-solution-of-the-pell-equation

"""

import math


def pell_solver_x(n):
    if math.sqrt(n)%1 == 0:
        return None
    x = int(math.sqrt(n))


    # calcul fraction continue :
    z = x = m = 1
    while n > m * m:
        m += 1
    m = y = m - 1
    l = ()
    while -z < x:
        x = (n - y * y) / x
        y += m
        l += y / x,
        y = m - y % x
        z = -1


def solvePell(n):
    if math.sqrt(n) %1 ==0:
        return 0,0  # si n est un carré, il n'existe pas de solution à l'équation
    x = int(math.sqrt(n))  # x prend la valeur de la partie entière de la racine de n
    y, z, r = x, 1, x << 1  # y, z, r, prennent la valeur de x, de 1, et décalage à gauche de 1 rang en binaire
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (n - y * y) // z
        r = (x + y) // z
        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r

        a, b = f2 * x + e2, f2
        if a * a - n * b * b == 1:
            return a, b



if __name__ == "__main__":
    max_x = 9
    i_max = 0

    for i in range(7,1001):
        x, y = solvePell(i)
        if x > max_x:
            max_x = x
            i_max=i
            print(i_max, len(str(max_x)), max_x)

    print(i_max)