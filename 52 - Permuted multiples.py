"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.

"""
from Timer import Timer

t = Timer()
t.start()

def sort_digits(n):
    """input a number n, get the sorted list associated"""
    temp_tab = [digit for digit in str(n)]
    temp_tab.sort()
    return temp_tab


def is_equal(l1, l2):
    """returns True if two lists are identical"""
    if len(l1) != len(l2):
        return False
    if set(l1) != set(l2):
        return False
    return True


def multiples_have_same_digits(n, nb_multiples):
    """
    Returns true if every multiple of n 2n, 3n, ...nb_multiples*n have
    exactly the same digits in a different order
    :param n:
    :param nb_multiples:
    :return: True, False
    """
    n_list_sorted = sort_digits(n)
    for i in range(2,nb_multiples+1):
        n_multiple_sorted = sort_digits(n*i)
        if not is_equal(n_list_sorted, n_multiple_sorted):
            return False
    return True


nb = 10000 # Starting point

while not multiples_have_same_digits(nb, 6):
    nb +=1

print(nb)
t.stop()
print(t.elapsed)