"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
from math import sqrt

primefactors = [2]

def is_prime(n):
    """Returns whether the number n is prime or not"""
    if n in primefactors:
        return True
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    primefactors.append(n)
    return True



def count_distinct_prime_factors(n):
    """returns the number of primes factor of n"""
    factors = {}
    cnt = 0
    div = int(sqrt(n))+1
    for i in range(div, 1, -1):
        if is_prime(i):
            if n % i == 0 :
                n = n/i
                if i not in factors:
                    factors[i] = None
                    cnt +=1
                if is_prime(n):
                    if n not in factors:
                        factors[n] = None
                        cnt+=1
    return cnt


def check_consecutive_numbers(n, nb_cons):
    """checks the nb_cons consecutive number, starting from n. We want to know if they have nb_cons prime factors"""
    # Initializing
    scan_n = [i for i in range (n, n+nb_cons)]
    scan_prime_factors = [count_distinct_prime_factors(nb) for nb in scan_n]
    to_compare = [nb_cons for i in range(nb_cons)]

    # then we want to move the scanners while scan_prime_factors does not have only nb_cons in it
    while scan_prime_factors != to_compare:
        # we pop the first number in both our scans
        scan_n.pop(0)
        scan_prime_factors.pop(0)
        # we add the following number in scan_n and add its number of prime factors to scan_prime_factors
        scan_n.append(scan_n[-1]+1)
        scan_prime_factors.append(count_distinct_prime_factors(scan_n[-1]))
        # # aaaannnnd we print the scans to make sure everything's all right
        # print(scan_n)
        # print(scan_prime_factors)
        # print("***")
    # With that loop we should be good so we just return the first number of scan_n
    return scan_n[0]


print(check_consecutive_numbers(50000, 4))



# def main():
#     nb = 50000
#     numbers = []
#     while True :
#         print(nb)
#         if check_consecutive_numbers(nb,4):
#             numbers.append(nb)
#             if len(numbers) > 4 :
#                 del(numbers[0])
#             if len(numbers) == 4:
#                 print(numbers)
#                 if numbers[0] == numbers[3] + 3:
#                     return numbers[0]
#         nb += 1
#
# print(main())