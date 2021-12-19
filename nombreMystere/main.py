import random

nbEssais = 10
over = False

def accueil():
    print("Bonjour, un nombre aléatoire entre 0 et 100 a été généré, tu as 10 essais pour tenter de le trouver. :\n")
    return random.randint(0, 100)

def essaisRestants():
    print(f"Il te reste {nbEssais} essais.")

def checkNbInput(input):
    if input < nombreMystere:
        print("C'est plus !\n")
        return False
    elif input > nombreMystere:
        print("C'est moins !\n")
        return False
    else :
        print(f"\nGagné en {10-nbEssais+1} essais!")
        return True


nombreMystere = accueil()
while nbEssais > 0 and over is not True:
    nbInput = int(input("Entrez un nombre : "))
    over = checkNbInput(nbInput)
    if over is not True:
        nbEssais -= 1
        essaisRestants()


