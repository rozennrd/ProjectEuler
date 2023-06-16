"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

def is_palindrom(n):
    temp_str = str(n)
    num = len(temp_str)
    for i in range(int(num/2)):
        if temp_str[i] != temp_str[num-i-1]:
            return False
    return True

sum_of_pal = 0
for n in range(1000000):
    if is_palindrom(n) and is_palindrom(format(n, 'b')):
        sum_of_pal += n
print(sum_of_pal)



# Autre solution trouvée en ligne :

# sum = 0
#
# for i in range(1, 1000000):
#     x = str(i)
#     y = "{0:b}".format(i)
#     if x == x[::-1] and y == y[::-1]:
#         sum += i
#
# print(sum)