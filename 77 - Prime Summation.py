"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?
"""

# générer les nombres premiers plus petits que le nombre en question
CACHE = {}

def is_prime(n):

    if n in CACHE:
        return CACHE[n]
    prime = True
    if n == 0 or 1:
        prime = False
        return prime
    for i in range(int(n**0.5)+1):
        if n//i ==0:
            prime = False

    CACHE[n] = prime  # true ou false
    return prime




primes = []


amount =100
memo = [[0 for i in range(amount+1)] for j in range(amount)]


WAYS = {0:1, 1:1}

def ways(tg, avc):
    """

    :param tg: target - the number we want to find the number of ways for
    :param avc:
    :return:
    """
    if is_prime(tg):
        primes.append(tg)
    if avc in WAYS:
        return WAYS[avc]

    t = tg
    if memo [t][avc] > 0 : return memo[t][avc]
    res = 0
    while tg >= 0:
        res = res + ways(tg, avc-1)
        tg = tg  - primes[avc]
    memo[t][avc]=res
    return res

amount = 2
w = 0
while w < 5000:
    w = ways(amount, len(primes))
    WAYS[amount] = w
    amount +=1
    print(amount, w)

print(amount)