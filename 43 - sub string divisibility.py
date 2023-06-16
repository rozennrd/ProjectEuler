"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations


def pandigital_0_9():
    """Générer les nombres pandigitaux de 0 à 9"""
    perm = []
    for i in permutations(range(10)):
        if i[0] != 0:
            nb = ""
            for digit in i:
                nb += str(digit)
            perm.append(nb)
    return perm


def check_substring_divisibilty(number):
    """
    with the number string as an input, checks if the number meets every criteria by checking all the subsequent substrings
    """
    prime_divisors = [2,3,5,7,11,13,17]
    prime_index = 0
    for i in range (1,8):
        if int(number[i:i+3]) % prime_divisors[prime_index] == 0:
            prime_index +=1
        else :
            return False
    return True



number_set = pandigital_0_9()
number_sum = 0
for number in number_set:
    if check_substring_divisibilty(number):
        number_sum += int(number)
print(number_sum)

