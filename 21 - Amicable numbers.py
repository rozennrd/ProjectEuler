from Timer import Timer
time = Timer()

time.reset()
time.start()

amicable = []
for a in range (2,10001):
    sa = 1
    for d in range(2, a-2):
        if a%d ==0:
            sa += d
    b = sa
    sb = 1
    for d in range(2, b-2):
        if b%d == 0:
            sb += d
    if b== sa and a == sb and a != b and a not in amicable:
        amicable.append(a)
        amicable.append(b)

print(amicable)
print(sum(amicable))

time.stop()
print(time.elapsed)

## Solution trouvée en ligne, plus rapide :
time.reset()
time.start()
def divsum(n):return sum([k+n/k for k in range(1,int(n**.5 + 1)) if n%k == 0])-n
print(sum([n for n in range(1,10000) if n==divsum(divsum(n)) if n!=divsum(n)]))
time.stop()
print(time.elapsed)


## Code lent, trouvé en ligne également ;
# tourne sur la machine d'origine en 50 secondes, tourne en 25 secondes
# sur une plus rapide... Pour comparaison :
time.reset()
time.start()

def div(s):
    l = []
    for n in range(1, s):
        if s%n == 0:
            l.append(n)
    return l

# def diva(lis):
#     a = 0
#     for n in lis:
#         a += n
#     return a

s = 0

for n in range(1,10001):
    a = sum(div(n))
    b = sum(div(a))
    if b == n and n != a:
        s += n

print("The sum of all amicable pairs under 10000 is: ", s)
time.stop()
print(time.elapsed)



q, r = divmod(10, 2)

q, r = divmod(n, k)