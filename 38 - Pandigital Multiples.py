"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""
from Timer import Timer

t = Timer()
t.start()
def is_pandigital(n_string):
    """
    Permet de vérifier si un nombre entré comme chaîne de caractère est pandigital
    Fonction vérifiée - fonctionne
    :param n_string:
    :return: boolean True or False
    """
    if len(n_string)!= 9:
        return False
    tab=[]
    for digit in n_string:
        if digit in tab or digit == '0':
            return False
        else:
            tab.append(digit)
    return True


def is_pandigital_2(n_string):
    numbers_n = list(n_string)
    return len(numbers_n) == len(set(numbers_n)) == 9


def has_common_digits(n, string):
    """
    Fonction vérifiant si un nombre a des chiffres en commun avec un autre nombre contenu dans une chaîne de caractères
    :param n: int
    :param string: chaine de caractère contenant un nombre
    :return: True or False
    """
    for digit in str(n):
        if digit in string:
            return True
    return False


product_sum = "" # initialisation de la chaîne contenant tous les nombres du produit.
max_pandigit = 0 # initialisation de la variable contenant le pandigital maximal trouvé


for n in range(2,10000):
    i = 1
    while len(product_sum) < 9:
        a = i * n
        if not has_common_digits(a, product_sum):
            product_sum += str(a)
            i+=1
        else:
            break
    if is_pandigital(product_sum): # vérifie si le nombre pandigital trouvé est plus grand que celui trouvé précédemment
        if int(product_sum) >= max_pandigit:
            max_pandigit = int(product_sum) # et assigne la valeur de ce pandigital au max le cas échéant.
    product_sum = "" # réinitialisation de product_sum si product_sum dépasse 9 chiffres

print(max_pandigit)

t.stop()
print(t.elapsed)


