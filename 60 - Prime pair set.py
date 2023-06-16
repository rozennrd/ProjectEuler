"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""
# todo : trop long, trouver un moyen d'optimiser
import time
from itertools import combinations

t1 = time.time()
def eratosthenes(n):
    """crée une array de booléens de longueur n, true pour les nombres premiers et False pour ceux qui ne le sont pas"""
    primes=[True for i in range(n+1)]
    primes[0] = False
    primes[1] = False

    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p +=1
    return set(i for i in range(n+1) if primes[i])


def is_prime(n):
    if n in primes:
        return True
    elif n < max(primes):
        return False
    else:
        if not n%2 or not n%3:
            return False
        i = 5
        stop = int(n ** 0.5)
        while i <= stop:
            if not n % i or not n % (i + 2):
                return False
            i += 6
    return True


cache_pairs = {}


def check_pair(n1, n2):
    # print(n1, n2)
    # print(int(str(n1) + str(n2)))
    # print(int(str(n2) + str(n2)))
    if (n1, n2) not in cache_pairs:
        condition = (is_prime(int(str(n1) + str(n2))) and is_prime(int(str(n2) + str(n1))))
        if condition:
            cache_pairs[(n1, n2)] = condition
        return condition
    else:

        return True


def prime_if_two_concatenated(l):
    """
    returns True if any two primes concatenated in any order is prime.
    We generate every combination in l, and check at every step if the concatenated number is prime
    """
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            check_pair(l[i], l[j])
    return True


maximum = 10000

primes = eratosthenes(maximum)
t2 = time.time()
print(t2-t1)
# prime_set = combinations(primes, 5)

lowest_sum = -1

# #
# for n in prime_set:
#     if prime_if_two_concatenated(n):
#         if lowest_sum < 0 or lowest_sum > sum(n):
#             lowest_sum = sum(n)
# print(lowest_sum)


primes_list = list(primes)
primes_list.sort()
# for i in range(len(primes_list)-1):
#     for j in range(i+1, len(primes_list)):
#         check_pair(primes_list[i], primes_list[j])
print(primes_list)


def check_list(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        for j in range(i, len(list_of_numbers)):
            if not check_pair(list_of_numbers[i], list_of_numbers[j]):
                return False
    return True


def check_quintuple():
    sums = []
    ln = len(primes_list)
    for a in primes:
        for b in primes:
            if b<a:
                continue
            if check_pair(a,b):
                for c in primes:
                    if c < b :
                        continue
                    if check_pair(b, c) and check_pair(a, c):
                        for d in primes:
                            if d < c:
                                continue
                            if check_pair(c, d) and check_pair(a, d) and check_pair(b, d):
                                for e in primes:
                                    if e < d :
                                        continue
                                    if check_pair(a, e) and check_pair(b, e) and check_pair(c, e) and check_pair(d, e):
                                        return a+b+c+d+e
                            # print(lst)

print(check_quintuple())

t3 = time.time()
# print(lowest_sum)
# print(cache_pairs)



print(t3-t2)
print(t3-t1)
