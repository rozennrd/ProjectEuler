# quel est le 10 001e nombre premiser ?
from Timer import Timer
t=Timer()
t.start()

# prime = []
# i = 2
# for i in range(2, 1000000000000):
#     test = True
#     for n in prime:
#         if i % n == 0:
#             test = False
#             break
#     if test:
#         prime.append(i)
#
#     if i > 10000:
#         try:
#             print(prime[10000])
#             break
#         except IndexError:
#             continue
# t.stop()
# print(t.elapsed)

# liste = []
# nombre = 2
#
# while len(liste) != 10000:
#     premier = True
#     for nb in liste :
#         if nombre % nb == 0:
#             premier = False
#             break
#     if premier :
#         liste.append(nombre)
#
# print(liste[-1])





primes = {}
primes_list = []

def is_prime(n):
    if n in primes:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        primes[n] = None
        primes_list.append(n)


i = 0
while len(primes_list) < 5000:
    is_prime(i)
    i+=1
    # print(len(primes_list))

print(primes_list[-1])

t.stop()
print(t.elapsed)