from bcolors import bcolors
from os import system, name
from random import randint


def Regle_Allumettes() -> None:
    """
    Cette procédure explique les règles du jeu Allumettes.
    Entrée : RIEN
    Sortie : RIEN
    """
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.jaune + "                     Règle du Jeu :")
    print("- Ce jeu se joue à 2 nombres.")
    print("- On dispose d'un tas de 20 allumettes.")
    print("-Chaque nombre à tour de rôle peut en prélever 1, 2 ou 3.")
    print("- Le perdant est celui qui prend la dernière allumette")
    print()
    print(bcolors.bleu + "Appuyer sur entrer pour continuer.")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        
    return None

def Affichage_Allumettes(allumettes : list[int]) -> None :
    """
    Cette procédure permet d'afficher les allumettes du jeu.
    Entrée : une liste d'entier de longueur 20

    Sortie : RIEN
    """
    print(bcolors.rouge + " ♦    "*len(allumettes) + bcolors.blanc) 
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    return None



def Jeu_Allumettes(joueur1 : str, joueur2 : str, difficulte1 : int, difficulte2 : int) -> bool:
    """
    Cette fonction met en place le jeu des allumettes.
    Entrée : 
        - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
        - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
        - `difficulte1`, un entier, qui représente la difficulté du joueur 1.
        - `difficulte2`, un entier, qui représente la difficulté du joueur 2.

    Sortie : 
        - un booléen pour donner le résultat du jeu.
    """
    allumettes : list[int]
    prenom : str
    compteur : int
    nombre : int
    resultat : int

    resultat = 0
    allumettes=[i for i in range(20)]     #initialisation des 20 allumettes
    print() #saut de ligne pour une meilleur visibilité
    print() #saut de ligne pour une meilleur visibilité

    #Boucle "tant que" qui fais tourner le jeu, le jeu s'arrête dès qu'il reste 1 allumette
    while len(allumettes) > 1 :      
        Affichage_Allumettes(allumettes)
        if resultat%2 !=0 :
            prenom = joueur2
        else:
            prenom = joueur1
            
        # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
        #sinon le joueur joue
        if prenom == "Ordinateur1":

            if difficulte1 == 1:
                if len(allumettes) == 3:
                    nombre = randint(1, 2)
                elif len(allumettes) == 2:
                    nombre = 1
                else:
                    nombre = randint(1, 3)
                
            else:

                if len(allumettes)%4 == 0:
                    nombre = 3
                elif len(allumettes)%4 == 1:
                    nombre = randint(1, 3)
                elif len(allumettes)%4 == 2:
                    nombre = 1
                elif len(allumettes)%4 == 3:
                    nombre = 2

        elif prenom == "Ordinateur2":

            if difficulte2 == 1:
                if len(allumettes) == 3:
                    nombre = randint(1, 2)
                if len(allumettes) == 2:
                    nombre = 1
                nombre = randint(1, 3)

            else:

                if len(allumettes)%4 == 0:
                    nombre = 3
                elif len(allumettes)%4 == 1:
                    nombre = randint(1, 3)
                elif len(allumettes)%4 == 2:
                    nombre = 1
                elif len(allumettes)%4 == 3:
                    nombre = 2

        else:

            nombre = int(input(f"{bcolors.cyan}{prenom}, combien d'allumettes voulez-vous enlever ? : " + bcolors.blanc))    # le joueur choisis combien d'allumette il veut enlever
            while nombre < 1 or nombre > 3:    #fiabilisation pour respecter les règles du jeu
                nombre = int(input(bcolors.rouge + "Vous ne pouvez enlever que 1, 2 ou 3 allumettes ! Recommencez : " + bcolors.blanc))

        resultat += 1

        for compteur in range(nombre):      #boucle "pour" permettant d'enlever le nombre d'allumette choisis par le joueur
            allumettes.pop(-1)

        system('cls' if name == 'nt' else 'clear')
        Affichage_Allumettes(allumettes)    # affichage du nombre d'allumette restant
        input(f"{bcolors.cyan}{prenom} a enlevé {nombre} allumettes. Appuyez sur entrer pour continuer. {bcolors.blanc}")
        system('cls' if name == 'nt' else 'clear')
        print() #saut de ligne pour une meilleur visibilité
        print() #saut de ligne pour une meilleur visibilité

        
        if len(allumettes) == 1 :    # condition "si/sinon" permettant de savoir si le nombre a gagner, sinon au tour du nombre2 de jouer
            if resultat%2 !=0 :
                print(f"{bcolors.vert}{joueur1}, Vous avez gagné !{bcolors.blanc}")
                print(f"{bcolors.rouge}{joueur2}, Vous avez perdu :( {bcolors.blanc}")
                return True
            else:
                print(f"{bcolors.vert}{joueur2}, Vous avez gagné !{bcolors.blanc}")
                print(f"{bcolors.rouge}{joueur1}, Vous avez perdu :( {bcolors.blanc}")

       
    return False