"""
Euler discovered the remarkable quadratic formula: n²+ n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n < 39. However, when is divisible by 41, and certainly when

is clearly divisible by 41.

The incredible formula was discovered, which produces 80 primes for the consecutive values

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

, where and

where
is the modulus/absolute value of
e.g. and

Find the product of the coefficients,
and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .
"""

# Calcul des nombres premiers :
primes = {}

def is_prime(n):
    if n < 1 :
        return False
    if n in primes:
        return True
    elif len([[i, n//i] for i in range(1,int(n**0.5) +1 ) if n%i ==0]) == 1:
        primes[n] = None
        return True
    else:
        return False

ab_count = {}
def check_quadratic_adds_to_count(a, b):
    n = 0
    count = 0
    while True:
        if is_prime(n**2 + a*n +b):
            count += 1
        else :
            break
        n += 1
    ab_count[(a, b)] = count


# calcul des séries de nombres premiers pour toutes les valeurs de a et b :
# vérifier la partie négative via des boucles est très long ; c'est pourquoi nous allons en même temps vérifier la
# partie positive et la partie négative ; devrait réduire par deux le temps pendant lequel le code tourne

# On rajoute aussi un cache pour stocker les combinaisons déjà évaluées ; dans ce dernier cas, on saute cette combinaison.
for a in range (1000):
    for b in range(1001):
        #On vérifie tous les cas possibles
        if (a,b) and (b,a) not in ab_count:
            check_quadratic_adds_to_count(a,b)
        if (-a,b) and (b, -a) not in ab_count:
            check_quadratic_adds_to_count(-a, b)
        if (a, -b) and (-b, a) not in ab_count:
            check_quadratic_adds_to_count(a, -b)
        if (-a,-b) and (-b,-a) not in ab_count:
            check_quadratic_adds_to_count(-a, -b)



#récupérer le tuple (a, b) où la valeur dans le dictionnaire est maximale
max_value = max(ab_count.values())
max_key = [key for key, value in ab_count.items() if value == max_value]
print(max_key, max_value, [v1 * v2 for v1,v2 in max_key]) # affiche a*b pour la plus longue série de nombres premiers


