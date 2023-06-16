"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
 adjacent digits) with the same digit, is part of an eight prime value family.
"""
from itertools import product

primes = {2:None}


def is_prime(n):
    """ Vérifie si un nombre est premier """
    if n in primes:
        return True
    if n < 2 :
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    primes[n] = None
    return True


def generate_numbers(nb_str):
    """A partir d'une str de type '53**6' génère tous les nombres obtenus en
    remplaçant '*' par un chiffre de 0 à 9"""
    liste_str = []
    if '*' not in nb_str:
        return None
    for i in range(10):
        new_str = ""
        for nb in nb_str:
            if nb == "*":
                new_str += str(i)
            else :
                new_str += nb
        if new_str[0] != "0":
            liste_str.append(new_str)
    return liste_str


def generate_strs(n):
    """génère toutes les strs de longueur n et retourne les nombres générés à partir de ces str """
    char = "*0123456789*"
    combinaisons = product(char, repeat=n)

    numbers_generated = []
    for nb in combinaisons:
        nombres= generate_numbers(nb)
        if nombres == None:
            pass
        else:
            numbers_generated.append(nombres)
    if numbers_generated != None:
        return numbers_generated


def nb_primes_in(liste):
    # print (liste)
    # print (liste == None)

    if liste == None:
        return 0
    nb_primes = 0
    for nb in liste:
        if is_prime(int(nb)):
            nb_primes +=1
    return nb_primes


def find_prime_series(nb_digits, nb_primes):
    for liste in generate_strs(nb_digits):
        if nb_primes_in(liste) == nb_primes:
            return liste[0]
    return None


print(find_prime_series(2, 6))

number_digits = 6
answer = False
while answer == False:
    if find_prime_series(number_digits, 8):
        answer = True
        print(find_prime_series(number_digits, 8))
    number_digits += 1


