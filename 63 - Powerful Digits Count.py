"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from Timer import Timer
if __name__ == "__main__":
    t=Timer()
    t.start()
    cnt = 0

    for n in range(1,30):
        for i in range(1,30):
            if len(str(i**n)) == n:
                cnt += 1
    t.stop()
    print(cnt)
    print(t.elapsed)



