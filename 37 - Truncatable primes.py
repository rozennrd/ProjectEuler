"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
 and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

primes = {}

def is_prime(n):
    if n in primes:
        return True
    elif n==1:
        return False
    elif len([[i, n//i] for i in range(1,int(n**0.5) +1 ) if n%i == 0]) == 1:
        primes[n] = None
        return True
    else:
        return False


# def truncated_is_prime:
#     for



def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return int(str(n)[:-1])

def is_truncatable(n):
    if not is_prime(n):
        return False
    right_truncated_num = n
    left_truncated_num = n
    while len(str(right_truncated_num)) > 1:
        right_truncated_num = truncate_right(right_truncated_num)
        left_truncated_num = truncate_left(left_truncated_num)
        if not is_prime(right_truncated_num) or not is_prime(left_truncated_num):
            return False
    return True


truncatables=[]
n = 11
while len(truncatables) != 11:
    if is_prime(n) and is_truncatable(n):
        truncatables.append(n)
    n+=1

print(sum(truncatables))


