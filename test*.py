

class Client :
    def __init__(self, telephone, adresse_mail):
        self.telephone = telephone
        self.adresse_mail = adresse_mail


class Entreprise(Client):
    def __init__(self, raison_sociale, adresse_mail, *args,**kwargs):
        super.__init__(self, *args, **kwargs)
        self.raison_sociale = raison_sociale
        self.adresse_mail = adresse_mail


def f(n):
    if n <= 1:
        return 1
    else:
        return f(n - 1) * n


i = 3
while i < 5:
    if i == 4:
        a = 2
    else:
        b = 1
    i += 2



class Voiture:
    def avancer(self):
        print("Je suis une voiture et je roule")


class Bateau:
    def avancer(self):
        print("Je suis un bateau et je flotte")


class VoitureAmphibie(Voiture, Bateau):
    pass


def perimetre(iterable):
    for n in iterable:
        yield 4 * n

liste = [5,6,7]
for i in perimetre(liste) :
    print(i)


class SousMarin(Bateau):
    pass

def perimetre(iterable):
    return map(lambda x: x * 4, iterable)

liste = [5,6,7]
for i in perimetre(liste) :
    print(i)


fonction_lambda = lambda x: x**2

print (fonction_lambda(5))




class Voiture:
    def avancer(self):
        print("Je suis une voiture et je roule")


class Bateau:
    def avancer(self):
        print("Je suis un bateau et je flotte")


class SousMarin(Bateau):
    pass


class VoitureAmphibie(SousMarin, Voiture):
    pass

v1 = VoitureAmphibie()
print(v1.avancer())