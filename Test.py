# a = 45 # entier (integer /int)
# b = 1235.235 # décimal (float)
# c = "bonjour"
# d = True
#
#
# print(56-25)
#
# print(b - a)
#
# liste = [a, b, c, d, 56]
# bob = [568, 45, 45]
# print(liste[0])
# print(bob[0])
# print(bob[1])
#
#
# bob[1] = 5
# print(bob)
#
# print(bob[0] - liste[0])
#
# #range = générateur, génère les nombres de 0 à ... n
#
# for i in range(5):
#     print(i)
#     print('dans la boucle')
# print("pas dans la boucle")
#
# print ('****')
# for i in range(5,10):
#     print(i)
#
# print('****')
# for i in range(5,15,2):
#     print(i)
#
# print('****')
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# print('****')
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 5:
#         break
#
#
#


from Timer import Timer


def function(n):
    return n+1


if __name__ == "__main__":
    t = Timer()
    t.start()
    sum = 0
    for i in range (100):
        sum += function(i)
    t.stop()
    print(t.elapsed)
    t.reset()
    t.start()
    sum = 0
    for i in range(100):
        sum += i+1
    t.stop()
    print(t.elapsed)
