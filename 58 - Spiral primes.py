# """
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If
# this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?
# """


# Tentative #2
"""
On se rend compte que pour obtenir les diagonales, il faut se déplacer d'un nombre de pas qui augmente à chaque fois,
et dont l'augmentation est prédictible et fonction du nombre de couches
"""
from Timer import Timer

prime_cache = {}


def is_prime(n):
    if n == 1 :
        return False
    if n in prime_cache:
        return True
    for nb in range(2,int(n**0.5)+1):
        if n % nb == 0:
            return False
    prime_cache[n] = None
    return True

#
# def check_number_of_primes(c):
#

cache_c = {}  # contenu : {n°_couche : (dernier n de la c, nb_primes à ce moment)}
def generate_diag_ratio():
    # Initialisation
    n = 1
    prime_cnt = 0
    cnt = 1
    c = 1

    while True:
        # if (c) in cache_c:
        #     n = cache_c[c][0]
        #     prime_cnt = cache_c[c][1]
        # else:
        for i in range(4):
            n = n + (2 * c)

            prime_cnt += is_prime(n)
            print(n, c, is_prime(n), prime_cnt, (2 * c) + 1)
            cnt +=1
            if prime_cnt / cnt < 0.1:
                return (2 * c) + 1
        c += 1

            # print(cnt, couche, n)
            # cache_c[c] = (n, prime_cnt)
    # while (prime_cnt/cnt) > 0.10:
    #     num_couche +=1
    #     generate_diag_ratio(num_couche)
    # return num_couche * 2 + 1

# def compute_sol():
#     ratio = 1
#     n = 10
#     while ratio > 0.1:
#         ratio = generate_diag_ratio(n)
#         n += 1
#
#     print(ratio)
#     print(n * 2 + 1)


if __name__ == "__main__":
    t = Timer()
    t.start()
    print(generate_diag_ratio())
    t.stop()
    print(t.elapsed)
    # print(generate_diag_ratio(3))

#
# # on commence à droite, puis on descend de 1, et ensuite on change les valeurs ; à chaque déplacement n += 1.
# # définition des mouvements :
#
# def move_right(y, x):
#     return y, x+1
#
# def move_down(y,x):
#     return y+1, x
#
# def move_left(y,x):
#     return y, x-1
#
# def move_up(y,x):
#     return y-1, x
#
# def change_value(y,x,n, spiral_):
#     """
#     Incrémente n et change la valeur dans le tableau à la position (x,y)
#     :param y: coordonnées dans la spirale sur l'axe y
#     :param x: coordonnées dans la spirale sur l'axe x
#     :param n: nombre par lequel remplacer la valeur spiral[y][x]
#     :return: None
#     """
#     n += 1
#     spiral_[y][x] = n
#     return n
#
#
#
# # def add_a_layer(spiral):
# #     length_of_
#
# def spiral_values(x, y, n, a, spiral_):
#     N = 1 # nombre de cases de chaque déplacement ; incrémenté de 2 tous les deux déplacements
#     while x < a: # tant que la case existe et est remplie (techniquement elle est remplie avec des zéros)
#         for i in range(N):
#             y, x = move_right(y, x)
#             if x==a or y==a:
#                 return spiral_
#             n = change_value(y,x,n, spiral_)
#         for j in range(N):
#             y, x = move_down(y, x)
#             if x==a or y ==a:
#                 return spiral_
#             n = change_value(y, x, n, spiral_)
#         N+=1
#
#         for i in range(N):
#             y, x = move_left(y, x)
#             if x == a or y == a:
#                 return spiral_
#             n = change_value(y,x,n, spiral_)
#         for j in range(N):
#             y, x = move_up(y, x)
#             if x == a or y == a:
#                 return spiral_
#             n = change_value(y, x, n, spiral_)
#         N+=1
#
#
# def add_one_layer_to_spiral(spiral):
#     initial_len = len(spiral[0])
#     size = initial_len + 2
#     new_spiral = [[0 for a in range(size)] for b in range(size)]
#     first_nb = 1  # initialisation
#     y_axis = int(size / 2)  # positions de début ; les positions changeront ppour générer la spirale
#     x_axis = int(size / 2)
#
#     new_spiral[y_axis][x_axis] = first_nb
#     spiral_values(x_axis, y_axis, first_nb, size, new_spiral)
#     return new_spiral
#
#
# prime_cache = {}
#
# def is_prime(n):
#     if n == 1 :
#         return False
#     if n in prime_cache:
#         return True
#     for nb in range(2,int(n**0.5)+1):
#         if n % nb == 0:
#             return False
#     prime_cache[n] = None
#     return True
#
#
# def check_prime_ratio(spiral):
#     # We count the number of numbers and the numbers of prime numbers, and we calculate a ratio out of it
#
#     nb_of_primes = 0
#     diag1 = []
#     diag2 = []
#     for i in range(len(spiral)):
#         diag1.append(spiral[i][i])
#         if is_prime(spiral[i][i]):
#             nb_of_primes += 1
#
#         diag2.append(spiral[i][-i-1])
#         if is_prime(spiral[i][-i-1]):
#             nb_of_primes += 1
#     # print("diag1 ", diag1)
#     # print("diag2 ", diag2)
#     print(nb_of_primes)
#     return nb_of_primes/(len(spiral[0])*2 -1)
#
#
# if __name__ == "__main__":
#     a = 26241
#
#     spiral = [[0 for i in range(a)] for j in range(a)]  # génération de la matrice
#
#     n = 1  # initialisation
#     y = int(a / 2)  # positions de début ; les positions changeront ppour générer la spirale
#     x = int(a / 2)
#
#     spiral[y][x] = n
#     spiral_values(x, y, n, a, spiral)
#     prime_ratio = check_prime_ratio(spiral)
#
#     # while prime_ratio > 0.1:
#     #     spiral = add_one_layer_to_spiral(spiral)
#     #     prime_ratio = check_prime_ratio(spiral)
#     #     print(len(spiral[0]), prime_ratio)
#
#     # for line in spiral:
#     #     for c in line :
#     #         print(f"{c:02d} ", end="")
#     #     print()
#     print("Done")
#     print(len(spiral[0]), prime_ratio)
