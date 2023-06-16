"""There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5    3) (version horizontale, normalement c'est vertical).

In general,
, where , , and.

It is not until
, that a value exceeds one-million:
.
How many, not necessarily distinct, values of
for , are greater than one-million?
"""
from Timer import Timer
t=Timer()
t.start()
def factorielle(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

count = 0
for n in range(23,101):
    for r in range(1, n+1):
        if (factorielle(n))/(factorielle(r) * factorielle(n-r)) > 1000000:
            count +=1

print(count)
t.stop()
print(t.elapsed)