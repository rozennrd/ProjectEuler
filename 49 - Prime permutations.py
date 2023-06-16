"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

"""

from itertools import permutations, combinations_with_replacement

cache = {2: None}


def is_prime(n):
    if n in cache:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    cache[n] = None
    return True


def convert(n):
    """prend en paramètre une liste ou un tuple et renvoie un entier"""
    n_str = ""
    for digit in n:
        n_str += str(digit)
    return int(n_str)


def verif_ecarts(liste):
    """fonction vérifiant tous les écarts entre les nombres d'une liste"""
    ecarts = {}
    for i in range(len(liste)):
        for j in range(len(liste)):
            if (liste[i], liste[j]) not in liste and (liste[j], liste[i]) not in liste and i < j:
                ecarts[(liste[i], liste[j])] = int(liste[j])- int(liste[i])
    if len(ecarts) != 0:
        return ecarts


def comparer_valeurs(dict):
    for key, val in dict:
        for key2, val2 in dict:
            if (key, val) != (key2, val2) and (val == key2):
                a= dict[(key, val)]
                b= dict[(key2, val2)]
                if a == b:
                    return (key,val, key2, val2)




def main():
    strs = []
    for digit_set in combinations_with_replacement(range(1, 10), 4):
        set_nbs = []
        i = 0

        for number in permutations(digit_set):
            nb = convert(number)
            i+=1
            if is_prime(nb):
                set_nbs.append(str(nb))

        if len(set_nbs) != 0:
            strs.append(set_nbs)
        # Nous avons maintenant les sets de nombres premiers qui se suivent. Nous devons vérifier chaque set de nombres
        # pour vérifier leurs écarts.
    ecarts = []
    valeurs =[]
    for elem in strs :
        ecarts.append(verif_ecarts(elem))
    for elem in ecarts:
        if elem is not None and comparer_valeurs(elem) is not None:
            valeurs.append(comparer_valeurs(elem))
    strings = []
    for elem in valeurs:
        strings.append(str(elem[0]) + str(elem[2]) + str(elem[3]))
    return strings




print(main())