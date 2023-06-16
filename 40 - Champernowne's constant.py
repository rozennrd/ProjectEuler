"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from Timer import Timer
t = Timer()
t.start()

constant = ""
for i in range(1,1000000):
    constant += str(i)

print( int(constant[0]) * int(constant[9]) * int(constant[99]) * int(constant[999]) * int(constant[9999]) * int(constant[99999]) * int(constant[999999]))

t.stop()
print(t.elapsed)