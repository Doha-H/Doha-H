import random

choix_utilisateur = input("Choisis l'une des options suivantes: Pierre/Papier/Ciseaux: ")
Possibiblites = ["pierre", "papier", "ciseaux"]
choix_ordinateur = random.choice(Possibiblites)

print(f"\nTu as choisi {choix_utilisateur}, l'ordinateur a choisi {choix_ordinateur}.\n")

if choix_utilisateur == choix_ordinateur:
    print(f"Les deux joueurs ont choisi {choix_utilisateur}. Match nul !")
elif choix_utilisateur == "pierre":
    if choix_ordinateur == "ciseaux":
        print("Tu as gagné !")
    else:
        print("Tu as perdu !")

elif choix_utilisateur == "papier":
    if choix_ordinateur == "pierre":
        print("Tu as gagné !")
    else:
        print("Tu as perdu !")

elif choix_utilisateur == "ciseaux":
    if choix_ordinateur == "papier":
        print("Tu as gagné !")
    else:
        print("Tu as perdu !")
