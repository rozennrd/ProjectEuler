# """
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
# exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
# multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be
# written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
# """
#
def is_pandigital(n1, n2, n):
    string_to_check = str(n1)+str(n2)+str(n)
    if len(string_to_check) == 9 and has_no_two_same_digits(int(string_to_check)) :
        return True
#
# def pandigit_product(n):
#     for i in range(1,int(n**0.5)+1):
#         if n % i ==0 and is_pandigital(str(i)+str(n)+str(n//i)):
#             return True
#     return False
#
# def main():
#     sum_pandigital = 0
#     for n in range(1111, 9999):
#         if pandigit_product(n):
#             sum_pandigital += n
#     return sum_pandigital
#
#
# ### On réessaye avec une autre méthode : on génère les nombres pandigitaux puis on teste s'il y a un produit dedans
# from itertools import permutations
# #
# pandigit = permutations("123456789",9)
# pan_number = []
# for num in pandigit :
#     for i in range(4): # sur 9 chiffres, le produit maximum qu'on aura sera peut être un nombre à 5 chiffres, et encore, c'est ambitieux
#         n = int("".join(num[len(num)-i-1:]))
#         diviseur = int("".join(num[:2]))
#         if n / diviseur == int("".join(num[2:len(num)-i-1])) and n not in pan_number:
#             pan_number.append(n)
# print(sum(pan_number))


def diviseurs(n):
    div = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            div.append((i, n//i))
    return div

def has_no_two_same_digits(n):
    tab = [0]
    for digit in (str(n)):
        if digit in tab or digit == '0':
            return False
        else:
            tab.append(digit)
    return True

pandigital_tab = []
for n in range(1000000):
    string=str(n)
    if has_no_two_same_digits(n):
        for tuples in diviseurs(n):
            n1, n2 = tuples
            if is_pandigital(n1, n2, n) and n not in pandigital_tab:
                pandigital_tab.append(n)
print(sum(pandigital_tab))

        #parcourir les nb jusqu'à un miliard, on vérifie si le nombre a des chiffres en double, si non on peut vérifier ses diviseurs, on concatène dans une str, et on regarde si c'est pandigital ;
#       si oui, on a un prd pandigital et on l'ajoute dans la liste

#
# pan = 0
# for i in range ()
#



#
# from time import time as t
#
# def prod_pan(n1, n2):
#     prod = list(str(n1 * n2))
#     n1 = list(str(n1))
#     n2 = list(str(n2))
#     z = sorted(prod + n1 + n2)
#     num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#     if z == num_list:
#         return True
#     else:
#         return False
#
# c = []
# t0 = t()
#
# for i in range(1, 100):
#     for j in range(100, 10000):
#         if prod_pan(i, j):
#             if (i * j) not in c:
#                 c.append(i * j)
#
# ans = sum(c)
# t1 = t()
#
# print(ans)
# print(t1 - t0)