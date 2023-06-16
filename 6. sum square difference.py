# consigne : trouver la différence entre la somme des carrés des 100 premiers
# entiers naturels, et le carré de la somme des 100 premiers entiers naturels


# calcul de la somme des carrés
sum_square = 0
for i in range(0,101):
    sum_square += i**2

print(sum_square)

# calcul du carré de la somme
square_sum = 0
for i in range(0,101):
    square_sum += i
square_sum = square_sum**2
print(square_sum)

print(square_sum - sum_square)

# Solution la plus optimale trouvée sur project euler:
a = 0
b = 0
for i in range(1,101):
    a += i**2
    b += i
print((b**2)-a)
