"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""


from math import sqrt
from Timer import Timer


def nombres_premiers(nb):

    nbList = []
    while nb % 2 == 0:
        nbList.append(2)
        # print(2)
        nb = nb/2

    for i in range(3, int(sqrt(nb))+1, 2):
        while nb % i == 0:
            nbList.append(i)
            nb = nb/i

    if nb > 2:
        nbList.append(nb)
    print(nbList)
    print(max(nbList))

t = Timer()
t.start()
nombres_premiers(13195)
# nombres_premiers(600851475143)
t.stop()
print(t.elapsed)

#
# def find_prime_factors(n):
#     remaining = n
#     primefactors = []
#     while remaining != 1:
#         if not primefactors:
#             i=1
#         else:
#             i=primefactors[len(primefactors)-1]-1
#         while i < remaining:
#             i += 1
#             if remaining % i == 0:
#                 remaining = remaining/i
#                 primefactors.append(i)
#                 break
#     return primefactors
#
# print(find_prime_factors(600851475143))

# # A function to print all prime factors of
# # a given number n
# def primeFactors(n):
#     # Print the number of two's that divide n
#     while n % 2 == 0:
#         print(2)
#         n = n / 2
#
#     # n must be odd at this point
#     # so a skip of 2 ( i = i + 2) can be used
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#
#         # while i divides n, print i ad divide n
#         while n % i == 0:
#             print(i)
#             n = n / i
#
#     # Condition if n is a prime
#     # number greater than 2
#     if n > 2:
#         print(n)


# Driver Program to test above function

# n = 315
# primeFactors(n)
