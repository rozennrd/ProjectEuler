#trouver la somme de tous les nombres primaires sous deux milions
from Timer import Timer
t=Timer()

t.start()
# prime = []
# i = 2
# for i in range(2, 2000000):
#     test = True
#     for n in prime:
#         if i % n == 0:
#             test = False
#             break
#     if test:
#         prime.append(i)
# t.stop()
# print (sum(prime))
# print(t.elapsed)


# Long !! Mesure = 776 secondes !!
# six mois plus tard, tentative de solution plus simple et rapide - environ 10 secondes

# def is_prime(n):
#     if n <2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i ==0:
#             return False
#     return True
#
#
# sum_of_primes = 0
# for n in range(2, 2000000):
#     if is_prime(n):
#         sum_of_primes+=n
# print(sum_of_primes)
# t.stop()
# print(t.elapsed)


primes = {}


def is_prime(n):
    if n in primes:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        primes[n] = None
        return True


s = 0
cpt = 0
for i in range(2, 2_000_000):
    if is_prime(i):
        s += i
        cpt += 1
print(s, cpt)
t.stop()
print(t.elapsed)