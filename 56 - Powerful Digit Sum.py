"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
from Timer import Timer
t=Timer()
t.start()
print(max(set(sum([int(n) for n in str(a**b)]) for a in range(100) for b in range(100))))
# for a in range(100):
#     for b in range(100):
#         cache.add(sum([int(n) for n in str(a**b)]))

# print(max(cache))
t.stop()
print(t.elapsed)