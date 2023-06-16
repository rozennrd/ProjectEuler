# class Vehicule:
#     """
#     Cette classe sert à xxx
#     les attributs sont yyyy
#     le poids est en tonnes
#     """
#     # poids = 1
#     # identifiant = None
#     couleur = "blanc"
#     # nombre_portes = 2
#     # hauteur = 1.2563
#     # longueur=2.3
#     # largeur = 3.6
#
#     def __init__(self, identifiant, largeur = 3.6,
#                  poids = 1, nombre_portes = None, hauteur = 1.2563,
#                  longueur=2.3):
#         self.identifiant = identifiant
#         self.largeur = largeur
#         self.poids = poids
#         self.nombre_portes = nombre_portes
#         self.hauteur = hauteur
#         self.longueur = longueur
#
#
# v1 = Vehicule(identifiant="abdsf")
# v1.couleur = "rouge"
# v1.poids = 2
# v1.hauteur = 2
# v1.longueur = 6
#
# # v2 = Vehicule(couleur="rouge")
#
# v3 = Vehicule(identifiant="AB25630", largeur=5)
#
#
# print(f"{v1.couleur}, {v3.couleur}")
#
# v1.longueur = 1.523  # en mètres
#
# print(v1.longueur)


class Vehicule:
    couleur = 'blanc'

    def __init__(self, couleur=None, identifiant=None):
        self.identifiant = identifiant
        if couleur is None:
            self.couleur = Vehicule.couleur
        else:
            self.couleur = couleur

    def afficher(self):
        print("Identifiant: %s" % self.identifiant)
        print("Couleur: %s" % self.couleur)

#
# class Voiture(Vehicule):
#     compteur = 0
#
#     def afficher(self):
#         super().afficher()
#         Voiture.compteur += 1
#         print(f"{Voiture.compteur} affichages de véhicules ont été réalisés")


# voit1 = Voiture()
# voit2 = Voiture("rouge", "2048 cd 04")
# voit2.afficher()
# voit1.afficher()



class Voiture(Vehicule):

    def __init__(self, nb_portes=5, *args, **kwargs):
        print(f"args (ARGumentS) : {args} , {type(args)}")
        print(f"kwargs (KeyWordARGumentS : {kwargs}, {type(kwargs)}")
        super().__init__(*args, **kwargs)
        self.nb_portes = nb_portes

    # accesseurs = getters
    def get_nb_portes(self):
        return self.nb_portes

    # manipulateurs = setters
    def set_nb_portes(self, nouvelle_valeur):
        if nouvelle_valeur < 12:
            self.nb_portes = nouvelle_valeur
        else:
            raise Exception


voit1 = Voiture()
voit2 = Voiture(9, "rouge", "2048 cd 04")
voit2.afficher()

# print(voit1.nb_portes)  # pas bien
print(voit1.get_nb_portes())

# voit1.nb_portes = 10  # pas bien
voit1.set_nb_portes(10)

v3 = Voiture(9, "vert", identifiant="1234")


class Singleton :
    __intance = None

    def __init__(self, instance):
        self.__intance = instance

    def get_instance(self):
        if Singleton.instance is None:
            Singleton.instance = Singleton("bonjour")
        return Singleton.instance

# pas d'autres astuces pour n'obtenir qu'une seule instance ?


