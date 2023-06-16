## CONSIGNE :
# If we list all the natural numbers below 10 that are multiples of 3 or
# 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
from Timer import Timer

timer = Timer()
timer.start()


def somme_3_5(n):
    sum = 0 # initialisation de la variable somme
    for i in range(0,n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            # print(i) #debug : vérification que les bons entiers sont
            # pris en compte
    return sum


print(somme_3_5(10)) #vérifie que la fonction retourne bien 23
print(somme_3_5(1000))
timer.stop()
print(timer.elapsed)



#version 2 - courte
timer.reset()
timer.start()
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
timer.stop()
print(timer.elapsed)