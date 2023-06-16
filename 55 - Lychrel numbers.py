"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""
from Timer import Timer


palindrom_cache = set()  # Caching helps gaining time (I gained 0.01 sec with this, not much but in more complex programs
# or if we had one million numbers to review, it could matter way more)


def is_a_palindrom(nb):
    if nb in palindrom_cache:
        return True
    nb_str = str(nb)
    if nb_str != nb_str[::-1]:
            return False
    palindrom_cache.add(nb)
    return True


def is_lychrel_number(nb):
    if str(nb)[-1] == 0:
        return False
    current_number = nb
    for i in range(50):
        reversed_number = int(str(current_number)[::-1])
        current_number = current_number + reversed_number
        if is_a_palindrom(current_number):
            return False
    return True


def count_lychrel_numbers():
    cnt =0
    for nb in range(11, 10001):
        if is_lychrel_number(nb):
            cnt +=1
    return cnt


# Found this : now it is sol 2
def is_Lychrel(n):
    n += int(str(n)[::-1])
    loop = 1
    while (str(n) != str(n)[::-1]) & (loop < 50):
        loop += 1
        n += int(str(n)[::-1])
    return str(n) != str(n)[::-1]


# Sol 3
def Lych(x):
    for i in range(0,49):
        a = str(x)
        x+= int(a[::-1])
        d = str(x)
        if d==d[::-1]:
            return True



def sol1():
    print("Sol n°1")
    t = Timer()
    t.start()
    print(count_lychrel_numbers())
    t.stop()
    print(t.elapsed)



def sol2():
    print("Sol n°2")
    t=Timer()
    t.start()
    sum(is_Lychrel(i) for i in range(10000))
    t.stop()
    print(t.elapsed)


def sol3():
    print("Sol n°3")
    t=Timer()
    t.start()
    count = 0
    for i in range(1, 10000):
        if Lych(i) != True:
            count += 1
    print(count)
    t.stop()
    print(t.elapsed)

sol1()
sol2()
sol3()