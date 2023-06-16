# faire la somme de tous les chiffres du nombre 100!
from functools import reduce
from Timer import Timer

time = Timer()

time.start()
fact=1
for i in range(1, 101):
    fact = fact * i

somme = sum(int(digit) for digit in str(fact))
# for digit in str(fact):
#     somme += int(digit)

print(sum)
time.stop()
print(time.elapsed)

# meilleure solution trouvée en une ligne sur le forum :
time.reset()
time.start()
print(reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))]))
time.stop()
print(time.elapsed)