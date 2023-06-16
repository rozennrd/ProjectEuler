"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import numpy as np
from Timer import Timer

print(np.cbrt(127035954683))
#
# if __name__ == "__main__":
#     n = 345
#     cubes = {n**3 : n for n in range(10000)}
#
#
#     while True:
#         # créer l'array numpy:
#         cpt = 0
#         for elem in permutations(str(n**3)):
#             if int("".join(elem) in cubes):
#                 cpt += 1
#             if cpt == 5:
#                 print(n)
#                 break
#             # print(int("".join(elem)))
#         n += 1
#         print(n)


# solution attendue : 127035954683 - le bruteforce ne fonctionnera pas
if __name__ == "__main__":
    t = Timer()
    t.start()
    cache = {}
    n = 345
    while True:
    # est-ce que n ** 3 est une permutation d'un nombre qu'on a déjà ?
        sorted_nb = "".join(sorted(str(n**3)))
        if sorted_nb not in cache:
            cache[sorted_nb] = []
        cache[sorted_nb].append(n ** 3)
        if len(cache[sorted_nb]) == 5:
            print(min(cache[sorted_nb]))

            break

        n +=1

    t.stop()
    print(t.elapsed)