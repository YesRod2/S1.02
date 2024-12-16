from bcolors import bcolors
from os import system, name

def Regle_Allumettes() -> None:
    """
    Cette procédure explique les règles du jeu Allumettes.
    Entrée : RIEN
    Sortie : RIEN
    """
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.jaune + "                     Règle du Jeu :")
    print("- Ce jeu se joue à 2 joueurs.")
    print("- On dispose d'un tas de 20 allumettes.")
    print("-Chaque joueur à tour de rôle peut en prélever 1, 2 ou 3.")
    print("- Le perdant est celui qui prend la dernière allumette")
    print()
    print(bcolors.bleu + "Appuyer sur entrer pour continuer.")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        
    return None

def Affichage_Allumettes(allumettes : list[int]) -> bool :
    """
    Cette procédure permet d'afficher les allumettes du jeu.
    Entrée : une liste d'entier de longueur 20
    Sortie : un booléen pour donner le résultat 
    """
    print(bcolors.rouge + " ♦    "*len(allumettes) + bcolors.blanc) 
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    print(" ‖    "*len(allumettes))
    return None



def Jeu_Allumettes() -> None:
    """
    Cette procédure met en place le jeu des allumettes.
    Entrée : RIEN
    Sortie : RIEN
    """
    allumettes : list[int]
    numero : int
    compteur : int
    joueur : int
    resultat : int

    resultat = 0
    allumettes=[i for i in range(20)]     #initialisation des 20 allumettes
    Affichage_Allumettes(allumettes)   #affichage du nombre d'allumette au début de la partie
    print() #saut de ligne pour une meilleur visibilité
    print() #saut de ligne pour une meilleur visibilité
    while len(allumettes) > 1 :      #Boucle "tant que" qui fais tourner le jeu, le jeu s'arrête dès qu'il reste 1 allumette
        if resultat%2 !=0 :
            numero = 2
        else:
            numero = 1
        joueur = int(input(f"{bcolors.cyan}joueur{numero}, combien d'allumettes voulez-vous enlever ? : " + bcolors.blanc))    # le joueur choisis combien d'allumette il veut enlever
        while joueur < 1 or joueur > 3:    #fiabilisation pour respecter les règles du jeu
            joueur = int(input(bcolors.rouge + "Vous ne pouvez enlever que 1, 2 ou 3 allumettes ! Recommencez : " + bcolors.blanc))
        resultat += 1

        for compteur in range(joueur):      #boucle "pour" permettant d'enlever le nombre d'allumette choisis par le joueur 
            allumettes.pop(-1)
        system('cls' if name == 'nt' else 'clear')
        Affichage_Allumettes(allumettes)    # affichage du nombre d'allumette restant
        print() #saut de ligne pour une meilleur visibilité
        print() #saut de ligne pour une meilleur visibilité


        if len(allumettes) == 1 :    # condition "si/sinon" permettant de savoir si le joueur a gagner, sinon au tour du joueur2 de jouer
            if resultat%2 !=0 :
                print(bcolors.vert + "joueur1, Vous avez gagné !" + bcolors.blanc)
                print(bcolors.rouge + "Joueur2, Vous avez perdu :( " + bcolors.blanc)
                return True
            else:
                print(bcolors.vert + "joueur2, Vous avez gagné !" + bcolors.blanc)
                print(bcolors.rouge + "Joueur1, Vous avez perdu :( " + bcolors.blanc)

       
    return False