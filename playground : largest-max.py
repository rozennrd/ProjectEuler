from Timer import Timer
#
timer1 = Timer()
# timer2 = Timer()
# timer3 = Timer()
#
# def alternate(A):
#   for v in A:
#     v_is_largest = True
#     for x in A:
#       if v < x:
#         v_is_largest = False
#         break
#     if v_is_largest:
#       return v
#   return None
#
# def largest(A):
#   my_max = A[0]
#   for idx in range(1, len(A)):
#     if my_max < A[idx]:
#       my_max = A[idx]
#   return my_max
#
# liste = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
#
# timer1.start()
# alternate(liste)
# timer1.stop()
# print(timer1.elapsed)
#
# timer2.start()
# largest(liste)
# timer2.stop()
# print(timer2.elapsed)
#
# timer3.start()
# max(liste)
# timer3.stop()
# print(timer3.elapsed)
#
#
# print("réinitialisation ; ici, algorithmes pour trier deux nombres du plus petit au plus grand")
#
# lst2=[1,5]
# timer1 = Timer()
# timer2 = Timer()
# timer3 = Timer()
#
#
# def sorting_two(A):
#   return tuple(sorted(A, reverse=True)[:2])
#
#
# def double_two(A):
#   my_max = max(A)
#   copy = list(A)
#   copy.remove(my_max)
#   return (my_max, max(copy))
#
# def mutable_two(A):
#   idx = max(range(len(A)), key=A.__getitem__)
#   my_max = A[idx]
#   del A[idx]
#   second = max(A)
#   A.insert(idx, my_max)
#   return (my_max, second)
#
# timer1.start()
# sorting_two(lst2)
# timer1.stop()
# print(timer1.elapsed)
#
# timer2.start()
# double_two(lst2)
# timer2.stop()
# print(timer2.elapsed)
#
# timer3.start()
# mutable_two(lst2)
# timer3.stop()
# print(timer3.elapsed)

timer1.start()
for i in range(1000000000):
  pass
timer1.stop()
print("Fini.")
print(timer1.elapsed)



def fact_equals(n):
  sum_fact = lambda x, y: x + y, [[int(dig)] for dig in str(n)]
  return sum_fact == n


timer1.reset()



for i in range(10):
  print("1")