from math import sqrt
from decimal import Decimal
from Timer import Timer


def find_period_length(p):
    if p == [0]:
        return 0
    print(p)
    strtoprocess = "".join([str(elem) for elem in p])

    for i in range(1, len(p)):
        strfind = strtoprocess[:i]
        strfind = strfind * (int(len(p) / i )+2)

        if strfind[:len(p)] == strtoprocess:
            return i
    return 0


def find_len_seq_of_sqrt(n):
    if Decimal.sqrt(Decimal(n)) == int(Decimal.sqrt(Decimal(n))):
        return [0]
    a = 1 / (Decimal.sqrt(Decimal(n)) - int(Decimal.sqrt(Decimal(n))))
    seq = [int(a)]
    for i in range(10):
        a = 1/(Decimal(a)-int(Decimal(a)))
        seq.append(int(a))
    return seq


def len_period_continuous_frac(n):
    z = x = m = 1
    while n > m * m:
        m += 1
    m = y = m - 1
    l = ()
    while -z < x:
        x = (n - y * y) / x
        y += m
        l += y / x,
        y = m - y % x
        z = -1
    return len(l)


if __name__ == "__main__":
    t = Timer()
    t.start()
    cnt = 0
    for i in range(2,10001):
        # if find_period_length(find_len_seq_of_sqrt(i)) %2 != 0:
        #     cnt += 1
        x = len_period_continuous_frac(i)
        if x != 0 and  x % 2 != 0:
            cnt +=1
    print(cnt)
    t.stop()
    print(t.elapsed)


    # https://codegolf.stackexchange.com/questions/6401/determining-the-continued-fractions-of-square-roots
    # https://web.math.princeton.edu/mathlab/jr02fall/Periodicity/mariusjp.pdf