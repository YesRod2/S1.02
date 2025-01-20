from Devinette import *
from Allumettes import *
from Morpion import *
from Menu_Joueur import *
from os import system , name
from bcolors import bcolors
from typing import BinaryIO
import pickle


def checkFileExistance(filePath)->bool:
    #Fonction qui teste la présence du fichier.
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False

def Charger_Sauvegarde(score : list[Joueurs]) -> list[Joueurs]:
    """
    Procédure qui charge le fichier binaire 
    ENTREE : la variable score, contenant les noms des joueurs et leurs scores
    SORITE : RIEN
    """
    f : BinaryIO
    if checkFileExistance("sauvegarde.bin"):
        f = open("sauvegarde.bin","rb") 
        score = pickle.load(f)
        system('cls' if name == 'nt' else 'clear')
        print(bcolors.vert + "Données Chargées.")
        print(bcolors.blanc + bcolors.jaune + "Appuyer sur Entrer pour continuer.")
        input()
        f.close()
    else:
        print(bcolors.rouge + "Fichier absent, aucune données chargées.")
        print(bcolors.blanc + bcolors.jaune + "Appuyer sur Entrer pour continuer.")
        input()
    return score

def sauvegarde(score : list[Joueurs]) -> None:
    """
    Procédure permattant de sauvegarder les joueurs et leurs scores dans un fichier binaire.
    ENTREE : 3 variables, de type ListeJeu, contenant le nom du joueur et son score.
    SORTIE : RIEN
    """
    f : BinaryIO

    f = open("sauvegarde.bin","wb")
    pickle.dump(score, f)
    f.close()
    print(bcolors.vert + "Fichier sauvegardé.")
    print(bcolors.blanc + bcolors.jaune + "Appuyer sur Entrer pour continuer.")
    input()
    return None


def Menu() -> int:
    
    ##Cette fonction permet d'afficher le menu de l'application. 
    #Paramètre d'Entrée : Rien
    ##Paramètre de Retour : un entier
    
    choix : int

    system('cls' if name == 'nt' else 'clear') # pour effacer le terminal, étant sur Windows ou linux/MacOS
    print(bcolors.blanc + bcolors.jaune +"Bonjour et Bienvenue dans notre application de jeu. Dans cette application, vous avez la possibilité de jouer à 3 jeux.")
    print("1. Ouvrir le menu des joueurs")
    print("2. Jeu de la Devinette")
    print("3. Jeu des Allumettes")
    print("4. Jeu du Morpion")
    print("5. Quitter l'application")
    print() #saut de ligne pour une meilleur visibilité
    choix = int(input(bcolors.blanc + bcolors.jaune + "Quel est votre choix ? : " + bcolors.blanc))

    while(choix < 1 or choix > 5):  #fiabilisation pour faire le bon choix de jeu ou pour quitter l'application
        print(bcolors.rouge + "Vous vous êtes trompé, veuillez relire le menu et recommencer s'il vous plaît. Merci ! " + bcolors.reset)
        choix = int(input(bcolors.blanc + bcolors.jaune + "Entrez à nouveau selon les choix au dessus : " + bcolors.blanc))


    return choix



if __name__ == "__main__" :
    choixJeu : int
    choix : int
    choix_joueur : int
    choix_classement : int
    nombre : int
    resultat : bool
    score : list[Joueurs]
    score2 : list[Joueurs]
    joueur1 : int
    joueur2 : int
    difficulte : int
    difficulte2 : int

    choixJeu = 0
    choix = 0
    choix_joueur = 0
    difficulte = 0
    difficulte2 = 0
    score = []
    score2 = []
    score=Charger_Sauvegarde(score)
    

    while choixJeu != 5: #boucle "tant que" faisant tourner le menu jusqu'à ce que les joueurs décident de quitter l'applcation
        choixJeu = Menu()
    

        if choixJeu == 1 :
            system('cls' if name == 'nt' else 'clear')
            while choix_joueur != 3:
                choix_joueur = Menu_Joueurs()

                if choix_joueur == 1:
                    if len(score) == 0 :
                        Ajouter_Joueurs(score)
                        score = score

                    else:
                        Ajouter_Joueurs(score2)
                        score += score2
                        score2 = []

                elif choix_joueur == 2 :
                    choix_classement = Menu_Classement()
                    if choix_classement == 1 :
                        score = Tri_Devinette(score)
                        Classement_Devinette(score)

                    elif choix_classement == 2 :
                        score = Tri_Allumette(score)
                        Classement_Allumette(score)

                    elif choix_classement == 3 :
                        score = Tri_Morpion(score)
                        Classement_Morpion(score)
                    input()
        
        choix_joueur = 0        
        if len(score) < 2 and choixJeu != 5 :
            print(bcolors.rouge + "Il vous manque des joueurs !, veuillez en ajouter avant d'accéder à la suite !")
            print(bcolors.cyan + "Appuyer sur Entrer pour continuer.")
            input()  

        elif choixJeu == 2 :  #condition si/sinon tout au long du menu pour démarrer le jeu choisis par les joueurs, est démarré ici ce qui est en lien avec le jeu 1

            system('cls' if name == 'nt' else 'clear')
            choix = 0
            while choix != 3: 
                print(bcolors.jaune + "Vous avez le choix entre lire les règles du jeu ou jouer.")
                choix = int(input("1- Lire les règles.\n2- Jouer au jeu.\n3- Revenir au menu Principal.\nVotre choix : "+ bcolors.blanc))  #les joueurs choisissent ce qu'ils veulent faire

                while  choix < 1 or choix > 3 :    #fiabilisation
                    print(bcolors.jaune + "Vous n'avez pas entré une bonne valeur !")
                    choix = int(input("1- Lire les règles.\n2- Jouer au jeu.\n3- Revenir au menu Principal.\nVotre choix : "+ bcolors.blanc))
                system('cls' if name == 'nt' else 'clear')

                if  choix == 1 :   #condition si/sinon qui soit donne les règle du jeu soit lance le jeu
                    Regle_Devinette()
                    input()
                    system('cls' if name == 'nt' else 'clear')

                elif choix == 2 :
                    joueur1 = Choisir_Joueur1(score, choixJeu)
                    joueur2 = Choisir_Joueur2(score, choixJeu)
                    system('cls' if name == 'nt' else 'clear')

                    # si un des joueurs est un ordinateur(=0) ou si les 2 joueurs ne sont pas des ordinateurs , on lance la fonction correspondante
                    if joueur1 == 0 or joueur2 == 0 :   

                        if joueur1 != 0 and joueur2 == 0 :

                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 2 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Devinette(score[joueur1-1].prenom, "Ordinateur2", difficulte)

                        elif joueur2 != 0 and joueur1 == 0 :
                            resultat = Jeu_Devinette("Ordinateur1", score[joueur2-1].prenom, difficulte)

                        else:
                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 2 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Devinette("Ordinateur1", "Ordinateur2", difficulte)

                    else:
                        resultat = Jeu_Devinette(score[joueur1-1].prenom, score[joueur2-1].prenom, difficulte)
                        if resultat :
                            score[joueur1-1].score_devinette += 1
                        else:
                            score[joueur2-1].score_devinette += 1
                
                
                    input()
                    system('cls' if name == 'nt' else 'clear')

            
        elif choixJeu == 3 :   #est démarré ici ce qui est en lien avec le jeu 2

            system('cls' if name == 'nt' else 'clear')
            choix = 0
            while choix != 3:
                print(bcolors.jaune + "Vous avez le choix entre lire les règles du jeu ou jouer.")
                choix = int(input("1- Lire les règles.\n2- Jouer au jeu.\n3- Revenir au menu Principal.\nVotre choix : "+ bcolors.blanc))

                while  choix < 1 or choix > 3 :
                    print(bcolors.jaune + "Vous n'avez pas entré une bonne valeur !")
                    choix = int(input("1- Lire les règles.\n2- Jouer au jeu.\n3- Revenir au menu Principal.\nVotre choix : "+ bcolors.blanc))
                system('cls' if name == 'nt' else 'clear')

                if  choix == 1 :   #condition si/sinon qui soit donne les règle du jeu soit lance le jeu
                    Regle_Allumettes() 
                    input()
                    system('cls' if name == 'nt' else 'clear')
                elif choix == 2 :
                    joueur1 = Choisir_Joueur1(score, choixJeu)
                    joueur2 = Choisir_Joueur2(score, choixJeu)
                    system('cls' if name == 'nt' else 'clear')

                    if joueur1 == 0 or joueur2 == 0 :   
                        if joueur1 != 0 and joueur2 == 0 :
                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 2 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Allumettes(score[joueur1-1].prenom, "Ordinateur2", difficulte, difficulte2)

                        elif joueur2 != 0 and joueur1 == 0 :
                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 1 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Allumettes("Ordinateur1", score[joueur2-1].prenom, difficulte, difficulte2)

                        else:
                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 1 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))

                            system('cls' if name == 'nt' else 'clear')

                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 2 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte2 = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))

                            resultat = Jeu_Allumettes("Ordinateur1", "Ordinateur2", difficulte, difficulte2)

                    else:
                        resultat = Jeu_Allumettes(score[joueur1-1].prenom, score[joueur2-1].prenom, difficulte, difficulte2)
                        if resultat :
                            score[joueur1-1].score_allumette += 1
                        else:
                            score[joueur2-1].score_allumette += 1
                    input()
                    system('cls' if name == 'nt' else 'clear')

        elif choixJeu == 4 :  #est démarré ici ce qui est en lien avec le jeu 3

            system('cls' if name == 'nt' else 'clear')
            choix = 0
            while choix != 3:
                print(bcolors.jaune + "Vous avez le choix entre lire les règles du jeu ou jouer.")
                choix = int(input("1- Lire les règles.\n2- Jouer au jeu.\n3- Revenir au menu Principal.\nVotre choix : "+ bcolors.blanc))

                while  choix < 1 or choix > 3 :    #fiabilisation

                    print(bcolors.jaune + "Vous n'avez pas entré une bonne valeur !")
                    choix = int(input("1- Lire les règles.\n2- Jouer au jeu.\n3- Revenir au menu Principal.\nVotre choix : "+ bcolors.blanc))
                system('cls' if name == 'nt' else 'clear')

                if  choix == 1 :   #condition si/sinon qui soit donne les règle du jeu soit lance le jeu
                    Regle_Morpion() 
                    input()
                    system('cls' if name == 'nt' else 'clear')
                elif choix == 2 :
                    joueur1 = Choisir_Joueur1(score, choixJeu)
                    joueur2 = Choisir_Joueur2(score, choixJeu)
                    system('cls' if name == 'nt' else 'clear')

                    if joueur1 == 0 or joueur2 == 0 :
                        if joueur1 != 0 and joueur2 == 0 :

                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 2 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Morpion(score[joueur1-1].prenom, "Ordinateur2", difficulte, difficulte2)

                        elif joueur2 != 0 and joueur1 == 0 :

                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 1 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Morpion("Ordinateur1", score[joueur2-1].prenom, difficulte, difficulte2)

                        else:

                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 1 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))

                            system('cls' if name == 'nt' else 'clear')

                            print(bcolors.jaune + "Voulez-vous que l'ordinateur 2 soit aléatoire(1) ou intelligent(2) ?")
                            difficulte2 = int(input("1- Aléatoire\n2- Intelligent\nVotre choix : "+ bcolors.blanc))
                            resultat = Jeu_Morpion("Ordinateur1", "Ordinateur2", difficulte, difficulte2)

                    else:
                        resultat = Jeu_Morpion(score[joueur1-1].prenom, score[joueur2-1].prenom, difficulte, difficulte2)
                        if resultat :
                            score[joueur1-1].score_morpion += 1
                        else:
                            score[joueur2-1].score_morpion += 1
                    input()
                    system('cls' if name == 'nt' else 'clear')

        elif choixJeu == 5: 
            system('cls' if name == 'nt' else 'clear')
            sauvegarde(score)
            print(bcolors.jaune + "Nous vous souhaitons une bonne journée et nous espérons que vous vous êtes bien Amusez ! À bientôt !" + bcolors.reset)