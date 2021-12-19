import random

difficulty = 1


def changeDifficulty():
    print("""Choisissez la difficulté :

    1 - Facile
    2 - Normale
    3 - Difficile
    4 - Impossible

    """)
    choix = input("Votre choix : ")

    if choix == "1":
        print("Difficulté changée pour Facile\n")
        return 0.6
    elif choix == "2":
        print("Difficulté changée pour Normale\n")
        return 1
    elif choix == "3":
        print("Difficulté changée pour Difficile\n")
        return 1.8
    elif choix == "4":
        print("Difficulté changée pour Impossible\n")
        return 3
    else:
        print("Choix inconnu\n")
        menuBase()

def menuBase():
    print("""Entrez votre choix dans la console :

    1 - Changer la difficulté
    2 - Lancer le jeu

    99 - Quitter le programme

    """)

    choix = input("Votre choix : ")

    if choix == "1":
        global difficulty
        difficulty = changeDifficulty()
        menuBase()
    elif choix == "2":
        mainJeu()
    elif choix == "99":
        print("Fermeture du programme...")
        exit(100)
    else:
        print("Choix inconnu")
        menuBase()

def mainJeu():
    print("C'est à votre tour de jouer...\n")
    ennemi = Ennemi(100*difficulty)
    personnage = Personnage()
    choix = 0

    while ennemi.get_alive() is True and personnage.get_alive() is True and choix != "9999":
        print(f"""Entrez votre choix dans la console :
        Ennemie : {ennemi.get_vie()} Point(s) de vie
        Vous : {personnage.get_vie()} Point(s) de vie

        1 - Attaquer l'ennemie
        2 - Boire une potion de santé

        """)

        choix = input("Votre choix : ")

        if choix == "1":
            personnage.attaque(ennemi)
        elif choix == "2":
            personnage.potion()
        else:
            print("Choix inconnu")
            exit(100)

        if personnage.get_alive() is True and ennemi.get_alive() is True:
            ennemi.attaque(personnage)


class Ennemi:

    def __init__(self, vie):
        self.__vie = vie
        self.__alive = True

    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        if vie > 0:
            self.__vie = vie
        else :
            self.set_alive(False)

    def get_alive(self):
        return self.__alive

    def set_alive(self, alive):
        self.__alive = alive

    def attaque(self, personnage):
        dmg = random.randint(1, 20)*(1/difficulty)
        personnage.set_vie(personnage.get_vie() - dmg)
        print(f"L'ennemie vous inflige {dmg} de dégats, il vous reste {personnage.get_vie()} points de vie.\n")
        if personnage.get_alive() is True:
            return True
        else:
            print("Vous êtes mort. GAME OVER.")
            return False


class Personnage:
    def __init__(self):
        self.__vie = 100
        self.__alive = True

    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        if vie > 0:
            self.__vie = vie
        else :
            self.set_alive(False)

    def get_alive(self):
        return self.__alive

    def set_alive(self, alive):
        self.__alive = alive

    def attaque(self, ennemie):
        dmg = random.randint(1, 20)*(1/difficulty)
        vieEnnemie = ennemie.get_vie()
        ennemie.set_vie(vieEnnemie - dmg)
        if ennemie.get_alive() is True:
            print(f"Vous infligez {dmg} de dégats à l'ennemie, il lui reste {ennemie.get_vie()} points de vie.\n")
            return True
        else:
            print("L'ennemie est mort, vous remportez le combat, félicitations!!")
            return False

    def potion(self):
        heal = random.randint(1, 20)
        self.set_vie(self.get_vie()+ heal)
        print(f"Vous vous soignez de {heal} points de vie, vous avez maintenant {self.get_vie()} points de vie.\n")





menuBase()