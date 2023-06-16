import numpy as np, matplotlib.pyplot as plt, time

def produit_matriciel(n):
    tdeb = time.time()
    taille = n*n
    m = np.array([i for i in range(taille)])
    m = m.reshape((n, n))
    pm= m@m

    tfin = time.time()
    return tfin - tdeb


print(produit_matriciel(10))

list = [1, 10, 100, 500, 1000, 1500, 2000, 2500, 3000]

tps = []
for n in list :
    tps.append(produit_matriciel(n))

print(tps)

plt.figure(figsize=(12,4))
plt.plot(list, tps,
         marker="x",
         c="red")

plt.show()