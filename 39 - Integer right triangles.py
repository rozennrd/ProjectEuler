"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from Timer import Timer

t = Timer()
t.start()


def is_a_sol(p, a):
    """
    à partir d'un périmètre et d'un côté : vérification de l'existence d'une solution telle que a, b et c peuvent
     être les côtés d'un triangle à angle droit. S'il existe une solution, on retourne true
    :param p: périmètre
    :param a: côté 1
    :return: True ou False
    """
    b = ((p**2) - (2*a*p)) / (2*p - 2*a)
    if b % 1 == 0 and b > 0:
        c = p - a - b
        if c % 1 == 0 and c > 0:
            return True
    return False


def number_of_sol(n):
    """
    for a given perimeter n we want to return the number of solutions : the number of sets of three numbers that satisfy
    the conditions for being the three sides a right angle triangle.
    :param n: int - périmètre donné
    :return: num_of_sol
    """
    num_of_sol = 0
    for a in range(1, int(n/3)):
        if is_a_sol(n, a):
            num_of_sol += 1
    return num_of_sol


def main():

    sol_dict = {}
    for p in range(1001):
        sol_dict[p] = number_of_sol(p)
    return max(sol_dict, key=sol_dict.get)


print(main())
t.stop()
print(t.elapsed)



