from os import system, name
from bcolors import bcolors
from random import choice
from Saisie import Saisir_Entier

def Regle_Morpion() -> None:
    """
    Procédure expliquant les règles du morpion.
    Entrée : RIEN
    Sortie : RIEN
    """
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.jaune + "                     Règle du Jeu :")
    print("- Ce jeu se joue à 2 joueurs.")
    print("- Chaque joueur pose sa marque (O ou X) à tour de rôle dans les cases d'une grille 3x3.")
    print("- Le premier qui aligne 3 marques a gagné.")
    print("- Si la grille est pleine et que personne n'a aligné 3 marques, c'est un match nul.")
    print()
    print(bcolors.bleu + "Appuyer sur entrer pour continuer.")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    
    return None

def TableauVide() -> list[list[str]]:
    """
    Fonction qui créer le tableau du morpion
    ENTREE : RIEN
    SORTIE : le tableau vide
    """
    Tableau : list[list[str]] 
    Tableau = [[" " for _ in range(3)]for _ in range(3)]
    
    #Affichage du Tableau
    print(f"|{Tableau[0][0]}|{Tableau[1][0]}|{Tableau[2][0]}|")
    print("-------")
    print(f"|{Tableau[0][1]}|{Tableau[1][1]}|{Tableau[2][1]}|")
    print("-------")
    print(f"|{Tableau[0][2]}|{Tableau[1][2]}|{Tableau[2][2]}|")
    

    return Tableau


def CasesVides(Tableau : list[list[str]]) -> list[list[int]]:
    """
    Fonction qui donne la liste des cases encore libres
    ENTREE : le tableau du morpion
    SORTIE : une liste de cases [Colonne, Ligne] (entre 1 et 3)
    """
    cases : list[list[int]]
    cases = []
    for colonne in range(3):
        for ligne in range(3):
            if Tableau[colonne][ligne] == " ":
                cases.append([colonne + 1, ligne + 1])
    return cases


def CoupIntelligent(Tableau : list[list[str]], symbole : str, symbole_adverse : str) -> list[int]:
    """
    Fonction qui choisit la meilleure case pour l'ordinateur intelligent
    ENTREE :
            - `Tableau`, le tableau du morpion.
            - `symbole`, le symbole de l'ordinateur ("X" ou "O").
            - `symbole_adverse`, le symbole de l'adversaire.
    SORTIE : une case [Colonne, Ligne] (entre 1 et 3)
    """
    cases : list[list[int]]
    case : list[int]
    marque : str

    cases = CasesVides(Tableau)

    #1) On cherche d'abord une case qui fait gagner l'ordinateur,
    #2) sinon une case qui empêche l'adversaire de gagner
    for marque in [symbole, symbole_adverse]:
        for case in cases:
            Tableau[case[0] - 1][case[1] - 1] = marque   #on essaie la case
            if VerifierGagne(Tableau):
                Tableau[case[0] - 1][case[1] - 1] = " "  #on annule l'essai
                return case
            Tableau[case[0] - 1][case[1] - 1] = " "      #on annule l'essai

    #3) Sinon on prend le centre s'il est libre
    if [2, 2] in cases:
        return [2, 2]

    #4) Sinon un coin libre
    for case in [[1, 1], [1, 3], [3, 1], [3, 3]]:
        if case in cases:
            return case

    #5) Sinon n'importe quelle case libre
    return choice(cases)


def Joueur(Tableau : list[list[str]], prenom : str, joueur1 : str, joueur2 : str, difficulte1 : int, difficulte2 : int, nb_tours : int) -> None:
    """
    Procédure permettant au joueur1 de choisir où placer son point
    ENTREE : 
            - `Tableau`, un tableau, qui représente le tableau du morpion.
            - `prenom`, une chaîne, qui représente le nom d'utilisateur du joueur.
            - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
            - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
            - `difficulte1`, un entier, qui représente la difficulté du robot 1.
            - `difficulte2`, un entier, qui représente la difficulté du robot 2.
            - `nb_tours`, un entier, qui représente le nombre de tours.

    SORTIE : RIEN
    """
    Colonne : int
    Ligne : int
    case : list[int]
    difficulte : int
    symbole : str
    symbole_adverse : str


    # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
    #sinon le joueur joue
    if prenom == "Ordinateur1" or prenom == "Ordinateur2":

        #Le joueur 1 joue les X et le joueur 2 joue les O
        if prenom == joueur1:
            symbole = "X"
            symbole_adverse = "O"
        else:
            symbole = "O"
            symbole_adverse = "X"

        if prenom == "Ordinateur1":
            difficulte = difficulte1
        else:
            difficulte = difficulte2

        #1 = aléatoire (parmi les cases libres), 2 = intelligent
        if difficulte == 1:
            case = choice(CasesVides(Tableau))
        else:
            case = CoupIntelligent(Tableau, symbole, symbole_adverse)
        Colonne = case[0]
        Ligne = case[1]

    else:
        print(f"{bcolors.blanc}{bcolors.cyan}{prenom}, à vous de jouer, entrez les coordonnées X (ligne) et Y (colonne) entre 1 et 3")
        Ligne = Saisir_Entier(f"{prenom}, entrez la coordonnée en X (entre 1 et 3) : {bcolors.blanc}" )
        Colonne = Saisir_Entier(f"{bcolors.blanc}{bcolors.cyan}{prenom}, entrez la coordonnée en Y (entre 1 et 3) : {bcolors.blanc}")
    

    #Vérifie si les coordonnées sont bonne (pas strictement inférieur à 1 et pas strictement supérieur à 3)
    while((Colonne < 1 or Colonne > 3) or (Ligne < 1 or Ligne > 3)):
        #Vérifie si le problème viens des coordonnées de la colonne
        if(Colonne < 1 or Colonne > 3):
            print(f"{bcolors.blanc}{bcolors.cyan}Vous avez entrée une coordonnée en colonne {bcolors.rouge}incorrect !")
            Colonne = Saisir_Entier(f"{bcolors.blanc}{bcolors.cyan}Entrez à nouveau une coordonnée de la colonne (compris entre 1 et 3): {bcolors.blanc}")
            #Ou si le problème viens des lignes
        elif(Ligne < 1 or Ligne > 3):
            print(f"{bcolors.blanc}{bcolors.cyan}Vous avez entrée une coordonnée en ligne {bcolors.rouge}incorrect !")
            Ligne = Saisir_Entier(f"{bcolors.blanc}{bcolors.cyan}Entrez à nouveau une coordonnée de la ligne (compris entre 1 et 3): {bcolors.blanc}")

    #Envois dans la fonction pour placer le pion du joueur sur la case entrée par le joueur
    JeuJoueur(Colonne, Ligne, Tableau, prenom, joueur1, joueur2, difficulte1, difficulte2, nb_tours)

#Fonction pour placer le pion du joueur 1 là où à été demandé par le joueur 1 
def JeuJoueur(Colonne : int, Ligne : int, Tableau : list[list[str]], prenom : str, joueur1 : str, joueur2 : str, difficulte1 : int, difficulte2 : int, nb_tours : int) -> list[list[str]]:
    """
    Fonction qui place le point du joueur1 
    ENTREE : 
            - `Colonne`, un entier, qui représente la colonne choisi par le joueur.
            - `Ligne`, un entier, qui représente la ligne choisi par le joueur.
            - `Tableau`, un tableau, qui représente le tableau du morpion.
            - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
            - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
            - `difficulte1`, un entier, qui représente la difficulté du robot 1.
            - `difficulte2`, un entier, qui représente la difficulté du robot 2.
            - `nb_tours`, un entier, qui représente le nombre de tours.

    SORTIE : 
            - `Tableau`, un tableau, qui représente le tableau du morpion.
    """
    #Vérifie si la case et vide
    system('cls' if name == 'nt' else 'clear')

    if prenom == joueur1:

        if (Tableau[Colonne - 1][Ligne - 1] == " "):
            #Si elle est vide, alors le programme place le pion du joueur 1
            Tableau[Colonne - 1][Ligne - 1] = "X"

        else :
            #Sinon si la case est déjà occupé, alors on lui dit qu'elle est déjà occupé
            system('cls' if name == 'nt' else 'clear')
            print(f"{bcolors.blanc}{bcolors.cyan}La ligne est déjà occupé !")
            #Et on lui redemande d'entrer à nouveau des coordonnées
            Joueur(Tableau, prenom, joueur1, joueur2, difficulte1, difficulte2, nb_tours)

    else:

        if (Tableau[Colonne - 1][Ligne - 1] == " "):
            #Si elle est vide, alors le programme place le pion du joueur 1
            Tableau[Colonne - 1][Ligne - 1] = "O"

        else :
            #Sinon si la case est déjà occupé, alors on lui dit qu'elle est déjà occupé
            system('cls' if name == 'nt' else 'clear')
            print(f"{bcolors.blanc}{bcolors.cyan}La ligne est déjà occupé !")
            #Et on lui redemande d'entrer à nouveau des coordonnées
            Joueur(Tableau, prenom, joueur1, joueur2, difficulte1, difficulte2, nb_tours)
    #Il retourne "Tableau" pour ensuite l'enregistrer en général
    return Tableau
       

def VerifierGagne(Tableau: list[list[str]]) -> bool:
    """
    Procédure vérifiant qui a gagné
    ENTREE : le tableau du morpion
    SORTIE : booléen, True si un joueur a gagné, False si non
    """
    joueurgagne : bool
    joueurgagne = False

    #Vérification en colonnes
    for compteur_i in range(0, 3):  
        if Tableau[compteur_i][0] == Tableau[compteur_i][1] == Tableau[compteur_i][2] and Tableau[compteur_i][1] in ["X", "O"]:
            joueurgagne = True
            return joueurgagne

    #Vérification en ligne
    for compteur_j in range(0,3):  
        if Tableau[0][compteur_j] == Tableau[1][compteur_j] == Tableau[2][compteur_j] and Tableau[0][compteur_j] in ["X", "O"]:
            joueurgagne = True
            return joueurgagne

    # Vérification des diagonales
    if Tableau[0][0] == "X" and Tableau[1][1] == "X" and Tableau[2][2] == "X" or Tableau[0][0] == "O" and Tableau[1][1] == "O" and Tableau[2][2] == "O":
        joueurgagne = True
        return joueurgagne
    if Tableau[2][0] == "X" and Tableau[1][1] == "X" and Tableau[0][2] == "X" or Tableau[2][0] == "O" and Tableau[1][1] == "O" and Tableau[0][2] == "O":
        joueurgagne = True
        return joueurgagne

    return joueurgagne


#Cette fonction affiche le tableau à chaque fois qu'un joueur va jouer
def AfficherTableau(Tableau: list[list[str]]) -> None:
    """
    Procédure Affichant le tableau du morpion
    ENTREE : le tableau du morpion
    SORTIE : RIEN
    """
    print(f"|{Tableau[0][0]}|{Tableau[1][0]}|{Tableau[2][0]}|")
    print("-------")
    print(f"|{Tableau[0][1]}|{Tableau[1][1]}|{Tableau[2][1]}|")
    print("-------")
    print(f"|{Tableau[0][2]}|{Tableau[1][2]}|{Tableau[2][2]}|")

    return None

def Jeu_Morpion(joueur1 : str, joueur2 : str, difficulte1 : int, difficulte2 : int) -> bool | None :
    """
    Fonction faisant tourner le jeu du morpion
    ENTREE :
            - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
            - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
            - `difficulte1`, un entier, qui représente la difficulté du robot 1.
            - `difficulte2`, un entier, qui représente la difficulté du robot 2.
    SORTIE : True si le joueur 1 gagne, False si le joueur 2 gagne, None en cas de match nul
    """

    joueurgagne : bool
    nb_tours : int
    prenom : str
    joueurgagne = False
    nb_tours = 0 

    system('cls' if name == 'nt' else 'clear')
    Tableau : list[list[str]] 
    Tableau = TableauVide()
    
    #Boucle while du tant que un joueur n'a pas gagné et que la grille n'est pas pleine (9 cases), on reste dedans
    while(not joueurgagne and nb_tours < 9):
        nb_tours += 1
        #Double vérification pour éviter de faire jouer les deux joueurs quand un à gagné
        if nb_tours % 2 == 1:
            prenom = joueur1
        else:
            prenom = joueur2
        
        if(joueurgagne == False):
            #Fonction pour faire jouer le joueur 1
            Joueur(Tableau, prenom, joueur1, joueur2, difficulte1, difficulte2, nb_tours)
            #Affichage du tableau pour montrer où le joueur à placé son pion
            AfficherTableau(Tableau)
            input()
            #Fonction pour vérifier si le joueur à gagné
            joueurgagne = VerifierGagne(Tableau)

            if (joueurgagne):
                if nb_tours % 2 == 1:
                    print(f"{bcolors.blanc}{bcolors.cyan}{joueur1} a {bcolors.vert}gagné {bcolors.blanc}{bcolors.cyan}la partie !")
                    print(f"{joueur2} a {bcolors.rouge}perdu !")
                else:
                    print(f"{bcolors.blanc}{bcolors.cyan}{joueur2} à {bcolors.vert}gagné {bcolors.blanc}{bcolors.cyan}la partie !")
                    print(f"{joueur1} a {bcolors.rouge}perdu !")

    #On renvoie le résultat de la partie
    if joueurgagne:
        return nb_tours % 2 == 1   #True si c'est le joueur 1 qui a joué le dernier coup

    print(f"{bcolors.blanc}{bcolors.cyan}La grille est pleine, c'est un {bcolors.jaune}match nul{bcolors.cyan} !")
    return None