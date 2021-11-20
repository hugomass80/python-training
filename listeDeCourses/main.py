


choix = 0
liste = ["Orange", "Citron", "Rosbeef"]


def afficher_liste():
    print("Votre liste de courses :\n")
    for idx, article in enumerate(liste):
        print(f"{liste.index(article)+1} - {article}")
    print()


def wait():
    wait = input("Appuyez sur une touche pour continuer...")


def choix_article():
    global article_todelete
    afficher_liste()
    article_todelete = (
        input("Entrez le nom de l'article que vous voulez enlever de votre liste de courses :")).lower().capitalize()


while choix != "99":
    print("""Entrez votre choix dans la console :

    1 - Ajouter un article à ma liste de courses
    2 - Enlever un article de ma liste de courses
    3 - Afficher ma liste de courses

    99 - Quitter le programme

    """)


    choix = input("Votre choix : ")

    if choix == "1":
        new = input("Entrez l'article à ajouter à votre liste de course : ")
        liste.append(new.lower().capitalize())
    elif choix == "2":
        choix_article()
        if article_todelete in liste:
            liste.remove(article_todelete)
            print(f"\nVous avez supprimé l'article {article_todelete} de votre liste.\n")
            wait()
        else:
            print(f"\nL'article {article_todelete} n'existe pas dans votre liste de courses\n")
            choix_article()
            wait()
    elif choix == "3":
        afficher_liste()
        wait()
    elif choix == "99":
        print("Fermeture du programme...")
    else:
        print("Choix inconnu")

print("Fin.")


