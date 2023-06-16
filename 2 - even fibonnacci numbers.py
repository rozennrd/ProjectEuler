#premier temps : génération d'une suite de fibonacci :
nb = range(1, 35)
fib = [0,1]


#implémentation de la suite de fibonacci dans un tableau
for n in nb:
    fib.append(fib[n-1]+fib[n])
print(fib)

def somme_fib_pairs():
    fib_sum = 0
    for number in fib:
        if number%2 ==0 :
            print(number)
            fib_sum += number
            if number > 4000000:
                break
    return fib_sum

print("nombre attendu",somme_fib_pairs())

#Version 2

fib = [0, 1,]
fib.append(fib[n - 1] + fib[n] for n in range(1, 55))

print(sum([number for number in fib if (number % 2 == 0) and (number >= 40000000)]))


