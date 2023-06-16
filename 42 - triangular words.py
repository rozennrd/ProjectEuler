"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a
word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""
from Timer import Timer
t= Timer()
t.start()


def cache(function):
    cache_dic = {}
    def patch(*args):
        if args not in cache_dic:
            cache_dic[args] = function(*args)
        return cache_dic[args]
    return patch


@cache
def is_triangular(n):
    """
    La page wikipédia des nombres triangulaires dit qu'un nombre est triangulaire si 8n + 1 est un carré.
    on vérifiera aussi si n
    est déjà dans le cache avant de calculer et résoudre l'équation. On utilise un dictionnaire pour optimiser l'accès.
    """
    if n < 0:
        return False
    if (8 * n + 1)**0.5 % 1 == 0:
        return True
    return False


def convert_to_number(word):
    return sum([ord(char) - 96 for char in word])


triangular_count = 0
with open("p042_words.txt","r") as file:
    fileconverted = file.read()
    words = [nom.strip('"').lower() for nom in fileconverted.split(',')]
    for word in words:
        if is_triangular(convert_to_number(word)):
            triangular_count += 1

print(triangular_count)

t.stop()
print(t.elapsed)


## Solution trouvée en ligne :

with open("p042_words.txt") as infile:
    words = infile.read().replace('"', '').split(",")

word_sums = [sum([(ord(x) - 64) for x in list(word)]) for word in words]
results = len([x for x in word_sums if not (((8 * x) + 1) ** .5) % 1])
print(results)
