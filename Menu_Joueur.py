from bcolors import *
from os import system, name
from Saisie import Saisir_Entier

class Joueurs :
    prenom : str
    score_devinette : int
    score_allumette :int
    score_morpion : int

    score_devinette = 0
    score_allumette = 0
    score_morpion = 0

def Menu_Joueurs() -> int:
    
    ##Cette fonction permet d'afficher le menu de l'application. 
    #Paramètre d'Entrée : Rien
    ##Paramètre de Retour : un entier
    choix : int
    system('cls' if name == 'nt' else 'clear')
    print(bcolors.blanc + bcolors.jaune + "Bonjour et Bienvenue dans le menu des joueurs. Dans ce menu, vous avez 2 choix possibles.")
    print("1. Ajouter des joueurs")
    print("2. Accéder au menu du classement")
    print("3. Quitter le menu des joueurs et revenir à l'application de jeu")
    print()
    choix = Saisir_Entier("Quel est votre choix ? : " + bcolors.blanc)

    while(choix < 1 or choix > 3):  #fiabilisation pour faire le bon choix de jeu ou pour quitter l'application
        print(bcolors.rouge + "Vous vous êtes trompé, veuillez relire le menu et recommencer s'il vous plaît. Merci ! " + bcolors.reset)
        choix = Saisir_Entier(bcolors.jaune + "Entrez à nouveau selon les choix au dessus : " + bcolors.blanc)
    return choix


def Menu_Classement() -> int :
    ##Cette fonction permet d'afficher le menu des classements des jeux 
    #Paramètre d'Entrée : Rien
    ##Paramètre de Retour : un entier
    choix : int
    system('cls' if name == 'nt' else 'clear')
    print(bcolors.blanc + bcolors.jaune + "1. Classement Devinette")
    print("2. Classement Allumette")
    print("3. Classement Morpion")
    choix = Saisir_Entier("Quel est votre choix ? : " + bcolors.blanc)

    while(choix < 1 or choix > 3):  #fiabilisation pour faire le bon choix de jeu ou pour quitter l'application
        print(bcolors.rouge + "Vous vous êtes trompé, veuillez relire le menu et recommencer s'il vous plaît. Merci ! " + bcolors.reset)
        choix = Saisir_Entier(bcolors.jaune + "Entrez à nouveau selon les choix au dessus : " + bcolors.blanc)
    return choix

def Ajouter_Joueurs(score_Joueur : list[Joueurs]) -> None:
    """
    Procédure ajoutant un nouveau joueur à l'application
    Entrée : la liste des joueurs, contenant le nom de chaque joueur et ses scores
    Sortie : RIEN
    """
    new_joueur : Joueurs
    prenoms : list[str]

    prenoms = [joueur.prenom for joueur in score_Joueur]   #noms des joueurs déjà inscrits

    new_joueur = Joueurs()
    new_joueur.prenom = input(bcolors.blanc + bcolors.cyan + "Quel est le nom du joueur que vous voulez ajouter ? : "+ bcolors.blanc).strip()

    #fiabilisation : le nom ne doit pas être vide, ni déjà pris (sinon on ne peut plus distinguer les joueurs)
    #"Ordinateur1" et "Ordinateur2" sont réservés aux robots
    while new_joueur.prenom == "" or new_joueur.prenom in prenoms or new_joueur.prenom in ["Ordinateur1", "Ordinateur2"]:
        print(bcolors.rouge + "Ce nom est vide, déjà utilisé ou réservé aux ordinateurs !")
        new_joueur.prenom = input(bcolors.blanc + bcolors.cyan + "Entrez un autre nom : " + bcolors.blanc).strip()

    score_Joueur.append(new_joueur)
    return None

def Classement_Devinette(score : list[Joueurs]) -> None :
    """
    Procédure permettant d'afficher le classement du jeu.
    ENTREE : la liste des joueurs, contenant le nom de chaque joueur et ses scores.
    SORTIE : rien
    """
    i : int
    n : int

    n = len(score)
    system('cls' if name == 'nt' else 'clear')
    if n == 0 :
        print()
        print(bcolors.jaune + "Vous n'avez pas de joueur, il n'y a donc pas de classement.")
    else:
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print()
        print(bcolors.blanc + bcolors.cyan +"        DEVINETTE")
        for i in range(n):
            print(f"{i+1:<4d} {score[i].prenom:<20s} {score[i].score_devinette:<4d}")
        print()
        print(bcolors.cyan + "Appuyer sur Entrer pour continuer.")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    return None

def Classement_Allumette(score : list[Joueurs]) -> None :
    """
    Procédure permettant d'afficher le classement du jeu.
    ENTREE : la liste des joueurs, contenant le nom de chaque joueur et ses scores.
    SORTIE : rien
    """
    i : int
    n : int

    n = len(score)
    system('cls' if name == 'nt' else 'clear')
    if n == 0 :
        print()
        print(bcolors.jaune + "Vous n'avez pas de joueur, il n'y a donc pas de classement.")
    else:
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print()
        print(bcolors.blanc + bcolors.cyan +"        ALLUMETTE")
        for i in range(n):
            print(f"{i+1:<4d} {score[i].prenom:<20s} {score[i].score_allumette:<4d}")
        print()
        print(bcolors.cyan + "Appuyer sur Entrer pour continuer.")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    return None

def Classement_Morpion(score : list[Joueurs]) -> None :
    """
    Procédure permettant d'afficher le classement du jeu.
    ENTREE : la liste des joueurs, contenant le nom de chaque joueur et ses scores.
    SORTIE : rien
    """
    i : int
    n : int

    n = len(score)
    system('cls' if name == 'nt' else 'clear')
    if n == 0 :
        print()
        print(bcolors.jaune + "Vous n'avez pas de joueur, il n'y a donc pas de classement.")
    else:
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print()
        print(bcolors.blanc + bcolors.cyan +"        MORPION")
        for i in range(n):
            print(f"{i+1:<4d} {score[i].prenom:<20s} {score[i].score_morpion:<4d}")
        print()
        print(bcolors.cyan + "Appuyer sur Entrer pour continuer.")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
        print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    return None

def Choisir_Joueur1(score : list[Joueurs], choixJeu : int) -> int :
    """
    Fonction permettant de choisir le joueur 1 pour jouer à un jeu
    ENTREE : la liste des joueurs, le choix du jeu 
    SORTIE : le joueur 1
    """
    joueur1 : int
    joueur1 = Saisir_Entier(bcolors.jaune + "Voulez vous que le joueur1 soit un robot ? (0 pour oui, 1 pour non) : "+ bcolors.blanc)
    while joueur1 != 0 and joueur1 != 1 :   #fiabilisation
        joueur1 = Saisir_Entier(bcolors.rouge + "Répondez par 0 (oui) ou 1 (non) : " + bcolors.blanc)
    if joueur1 == 0 :
        return joueur1
    else :
        if choixJeu == 2 :
            score = Tri_Devinette(score)
            Classement_Devinette(score)
        elif choixJeu == 3 :
            score = Tri_Allumette(score)
            Classement_Allumette(score)
        elif choixJeu == 4 :
            score = Tri_Morpion(score)
            Classement_Morpion(score)
    print()
    print()
    print(bcolors.cyan + "Le choix du joueur se fait avec son id.")
    print("Regardez le classement ci-dessus pour connaitre votre id.")
    print()
    joueur1 = Saisir_Entier("Quel est l'id du joueur 1 : " + bcolors.blanc)
    while joueur1 < 1 or joueur1 > len(score) :   #fiabilisation : l'id doit exister dans le classement
        joueur1 = Saisir_Entier(f"{bcolors.rouge}Cet id n'existe pas, entrez un id entre 1 et {len(score)} : {bcolors.blanc}")
    
    return joueur1

def Choisir_Joueur2(score : list[Joueurs], choixJeu : int, joueur1 : int = 0) -> int :
    """
    Fonction permettant de choisir le joueur 2 pour jouer à un jeu
    ENTREE : la liste des joueurs, le choix du jeu, l'id du joueur 1 (0 si c'est un robot)
    SORTIE : le joueur 2
    """
    system('cls' if name == 'nt' else 'clear')
    joueur2 : int
    joueur2 = Saisir_Entier(bcolors.jaune + "Voulez vous que le joueur2 soit un robot ? (0 pour oui, 1 pour non) : "+ bcolors.blanc)
    while joueur2 != 0 and joueur2 != 1 :   #fiabilisation
        joueur2 = Saisir_Entier(bcolors.rouge + "Répondez par 0 (oui) ou 1 (non) : " + bcolors.blanc)
    if joueur2 == 0 :
        return joueur2
    if choixJeu == 2 :
        score = Tri_Devinette(score)
        Classement_Devinette(score)
    elif choixJeu == 3 :
        score = Tri_Allumette(score)
        Classement_Allumette(score)
    elif choixJeu == 4 :
        score = Tri_Morpion(score)
        Classement_Morpion(score)
    print()
    print()
    print(bcolors.cyan + "Le choix du joueur se fait avec son id.")
    print("Regardez le classement ci-dessus pour connaitre votre id.")
    print()
    joueur2 = Saisir_Entier("Quel est l'id du joueur 2 : " + bcolors.blanc)
    #fiabilisation : l'id doit exister et le joueur 2 ne peut pas être le joueur 1
    while joueur2 < 1 or joueur2 > len(score) or joueur2 == joueur1 :
        if joueur2 == joueur1 :
            print(bcolors.rouge + "Ce joueur est déjà le joueur 1 !")
        joueur2 = Saisir_Entier(f"{bcolors.rouge}Entrez un id entre 1 et {len(score)} : {bcolors.blanc}")
    
    return joueur2

def Tri_Devinette(score : list[Joueurs]) -> list[Joueurs]:
    """
    Tri le tableau de façon tri à bulle
    ENTREE : le tableau contenant les joueurs et leurs scores
    SORTIE : le tableau trié par score décroissant
    """
    n : int
    p : int
    i : int
    joueurTemp : Joueurs
    echange : bool

    joueurTemp = Joueurs()
    n = len(score)
    p = n-1
    echange = True
    while echange and p>0:
        echange = False
        for i in range(0,p):
            if score[i].score_devinette < score[i+1].score_devinette :
                joueurTemp = score[i+1]
                score[i+1] = score[i]
                score[i]= joueurTemp
                echange = True
        p = p-1
    return score

def Tri_Allumette(score : list[Joueurs]) -> list[Joueurs]:
    """
    Tri le tableau de façon tri à bulle
    ENTREE : le tableau contenant les joueurs et leurs scores
    SORTIE : le tableau trié par score décroissant
    """

    n : int
    p : int
    i : int
    joueurTemp : Joueurs
    echange : bool

    n = len(score)
    p = n-1
    echange = True
    while echange and p>0:
        echange = False
        for i in range(0,p):
            if score[i].score_allumette < score[i+1].score_allumette :
                joueurTemp = score[i+1]
                score[i+1] = score[i]
                score[i]= joueurTemp
                echange = True
        p = p-1
    return score

def Tri_Morpion(score : list[Joueurs]) -> list[Joueurs]:
    """
    Tri le tableau de façon tri à bulle
    ENTREE : le tableau contenant les joueurs et leurs scores
    SORTIE : le tableau trié par score décroissant
    """
    
    n : int
    p : int
    i : int
    joueurTemp : Joueurs
    echange : bool

    n = len(score)
    p = n-1
    echange = True
    while echange and p>0:
        echange = False
        for i in range(0,p):
            if score[i].score_morpion < score[i+1].score_morpion :
                joueurTemp = score[i+1]
                score[i+1] = score[i]
                score[i]= joueurTemp
                echange = True
        p = p-1
    return score