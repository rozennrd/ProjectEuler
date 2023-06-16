## 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


def smallest_multiple(nb):
    n = 14298918
    compte= 0#initialisation
    while compte!= nb:
        compte = 0
        n +=1
        for i in range (1, nb+1):
            if(n%i)!=0:
                continue
            else:
                compte += 1
        print(compte, n)
    print("le nombre recherché est ", n)


smallest_multiple(20)
