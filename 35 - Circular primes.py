"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from Timer import Timer
t = Timer()

t.start()
primes = {}

def is_prime(n):
    if n in primes:
        return True
    elif len([[i, n//i] for i in range(1,int(n**0.5) +1 ) if n%i == 0]) == 1:
        primes[n] = None
        return True
    else:
        return False


def cycle(n):
    """
    fonction qui prend en paramètre un nombre et renvoie les nombres
    composés des mêmes chiffres dans le même ordre mais ne commençant
    pas au même point.
    :param n:
    :return:
    """
    temp_str = str(n)
    list_cycle = []
    while True:
        list_cycle.append(temp_str)
        temp_str = temp_str + temp_str[0]
        temp_str = temp_str[1:]
        if temp_str == list_cycle[0]:
            list_cycle_num = [int(i) for i in list_cycle]
            return list_cycle_num

def cycle_is_prime(n):
    for x in cycle(n):
        if not is_prime(x):
            return False
    return True

circular = []
for x in range(2, 1000000):
    if x not in circular and is_prime(x) and cycle_is_prime(x):
        tab = cycle(x)
        for n in tab:
            circular.append(n)
t.stop()
print(circular)
print(len(circular))
print(t.elapsed)



"""
Autre solution trouvée, 15 secondes sur le pc de l'OP 
"""
# import math
# import timeit
#
# def numberRotation(n):
#     num = str(n)
#     rotationList = []
#     for i in range(len(num)):
#         num = num[-1] + num[:-1]
#         rotationList.append(int(num))
#     return rotationList
#
#
# def isPrime(n):
#     prime = True
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n))+1):
#             if n % i == 0:
#                 prime = False
#         return prime
#
# def sieveofE(n):
#     prime = [True for p in range(n + 1)]
#     p = 2
#     while p ** 2 <= n:
#         if prime[p]:
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     prime[0] = False
#     prime[1] = False
#     return [i for i, p in enumerate(prime) if p]
#
#
# t1 = timeit.default_timer()
#
# primeList = sieveofE(1000000)
# resultList = []
#
# for p in primeList:
#     valid = True
#     numberRotationList = numberRotation(p)
#     for i in numberRotationList:
#         if not isPrime(i):
#             valid = False
#     if valid:
#         for j in numberRotationList:
#             if j not in resultList:
#                 resultList.append(j)
#         valid = True
#
# print(len(resultList))
#
# t2 = timeit.default_timer()
# print(t2-t1)


"""
Solution 3, 0.15 secondes
"""
# from sympy.ntheory import isprime
#
#
# def addprimerot(n):
#     num = str(n) * 2
#     siz = len(num) // 2
#
#     if "2" in num or "4" in num or "6" in num or "8" in num or "0" in num or "5" in num:
#         return 0
#     else:
#         for i in range(0, siz):
#             tester = int(num[i : i + siz])
#             if not isprime(tester):
#                 return 0
#
#     return 1
#
#
# check = 11
# max_limit = 1_000_000
# qtde = 4
#
# while check <= max_limit:
#     if check % 6 in (1, 5):
#         qtde += addprimerot(check)
#     check += 2
#
#
# print(qtde)  # 55