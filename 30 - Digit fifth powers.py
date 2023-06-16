
digits_pow = {n:n**5 for n in range(10)}

# on veut savoir combien de nombres peuvent être écrits comme la somme de leurs chiffres à la cinquième puissance.
fifth_pow = []
for i in range(2, 10**6):
    nb = [int(c) for c in str(i)]

    # génération des str pour concaténer les éléments du tupple généré parla fonction itertools
    nombre = int("".join([str(digit) for digit in nb]))

    if nombre == sum(digits_pow[dig] for dig in nb):
        print(nombre)
        fifth_pow.append(nombre)

print(fifth_pow)
print(sum(fifth_pow))

