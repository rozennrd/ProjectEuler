"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import fractions

# from decimal import Decimal
# # génération du tableau
# dictionnaire = {}
# for n in range(1,1000):
#     dictionnaire[n] = [digit for digit in str(Decimal(1)/Decimal(n))[2:]] #si ce chiffre n'est pas égal au premier chiffre,et le suivant n'est pas égal au deuxième
#
#
#
# for n in dictionnaire :
#     i = 0
#     diff = 1
#     slow = dictionnaire[n][i]
#     fast = dictionnaire[n][i+diff]
#     count=1
#     while fast != slow:
#         diff += 1
#         count += 1
#     if fast == slow :
#         a = diff
#         for s in range(a):
#             i += 1
#             diff+=1
#             if slow != fast :
#                 count += s
#
#                 break;
# print(n + 1)



# idée pour demain : implémenter la division comme on la posait, et détecter les répétitions dans le reste pour
# détecter les répétitions dans le pattern ; implémenter un compteur qui permet de voir la longueur de la chaîne
longueurchaine = []

for n in range(1, 1000):
    count = 0
    q, r = divmod(1, n)
    restes = []
    while r not in restes : 
        restes.append(r)
        q, r = divmod(r*10, n)
        count += 1
    longueurchaine.append(count)        

print(longueurchaine.index(max(longueurchaine))+1)