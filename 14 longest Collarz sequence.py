from Timer import Timer# ajout d'un timer pour mesurer le temps que prend chaque solution,
# et pour mesurer les solutions aux prochains problèmes...

time=Timer()

time.start()
len_chains_to_one_million = {}

def collatz_chain(n):
    len_collatz = 0
    N=n
    while n != 1 :
        if n in len_chains_to_one_million:
            len_collatz += len_chains_to_one_million[n]
            break
        else :
            len_collatz += 1
            if n%2 == 0:
                n = n/2
            else:
                n = 3 * n + 1
    len_chains_to_one_million[N]=len_collatz
    return len_collatz




for i in range(2, 1000000):
    collatz_chain(i)


maximum = max(len_chains_to_one_million.values())
for k, v in len_chains_to_one_million.items():
    if v==maximum:
        print(k)
        break
time.stop()
print(time.elapsed)