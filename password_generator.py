# Il s'agit d'un programme permettant de générer un mot de passe aléatoire.
# Ce programme offre la possibilité à l'utilisateur de choisir les conditions nécessaires pour rendre son mot de passe robuste. 
# (longueur minimale, chiffres, caractères spéciaux).

# Ici, je suis amenée à mettre en pratique l'importation de modules, une boucle while, des conditionnelles if/elif. 
# Je définis ma propre fonction generate_passwod() et j'utilise une fonction input() pour recevoir les entrées de l'utilisateur.


import random
import string  # Importation du module string pour utiliser des chaînes de caractères prédéfinies

def generate_password(min_Length, numbers=True, special_characters=True):
    letters = string.ascii_letters  # cette constante représente l'ensemble des lettres de l'alphabet, minuscules et majuscules
    digits = string.digits          # celle-ci repésente les chiffres de 0 à 9
    special = string.punctuation    # celle-ci repésente les caractères de ponctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_Length:    # Boucle pour générer le mot de passe jusqu'à ce qu'il réponde aux conditions spécifiées
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)?").lower() == "y"
has_special = input("Do you want to have special characters (y/n)?").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is", pwd)
