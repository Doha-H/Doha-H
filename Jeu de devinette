# Le but du jeu est de deviner un nombre que le programme a généré aléatoirement. 
# Dans ce programme je fais appel à un module, je défini des fonctions, j'utilise une boucle while, des conditions if/elif et j'utilise des f-strings


import random  # Importation du module random pour générer des nombres aléatoires

def devine(x):  # Définition d'une fonction appelée "devine" prenant un argument x
    nombre_aleatoire = random.randint(1, x)  # Génère un nombre aléatoire entre 1 et x inclus
    devine = 0  # Initialise la variable devine à 0
    while devine != nombre_aleatoire:  # Utilisation d'une boucle while perpettant au programme de faire deviner tant que le nombre proposé n'est pas égal au nombre aléatoire.
        devine = int(input(f'Devinez un nombre entre 1 et {x} : '))  # Demande à l'utilisateur de deviner un nombre
        if devine < nombre_aleatoire:  # Vérifie si le nombre deviné est inférieur au nombre aléatoire
            print('Désolé, le nombre est trop petit. Essayez encore')  
        elif devine > nombre_aleatoire:  # Vérifie si le nombre deviné est supérieur au nombre aléatoire
            print('Désolé, le nombre est trop grand. Essayez encore') 

    print(f'Bien joué ! Vous avez deviné le nombre {nombre_aleatoire} correctement !')  # utilisation d'une f-string afin d'insérer la variable (nombre deviné) dans le message de félicitations

devine(20)  # Appel de la fonction devine avec 20 comme argument (c'est la limite supérieure pour la plage de nombre à deviner)
