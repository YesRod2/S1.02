from os import system, name
from bcolors import bcolors


def Regle_Morpion() -> None:
    """
    Procédure expliquant les règles de la devinette.
    Entrée : RIEN
    Sortie : RIEN
    """
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.jaune + "                     Règle du Jeu :")
    print("- Ce jeu se joue à 2 joueurs.")
    print("- Chaque joueur pose sa marque (O ou X) à tour de rôle dans les cases d'une grille 3x3.")
    print("- Le premier qui aligne 3 marques a gangé.")
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


def Joueur1(Tableau : list[list[str]]) -> None:
    """
    Procédure permettant au joueur1 de choisir où placer son point
    ENTREE : le tableau du morpion
    SORTIE : RIEN
    """
    Colonne : int
    Ligne : int

    #Demande à l'utilisateur d'entrer les coordonnées d'où il veut jouer
    print("Joueur 1 (X), à vous de jouer, entrez les coordonnées X (ligne) et Y (colonne) entre 1 et 3")
    Ligne = int(input("Joueur 1 (X):Entrez la coordonnée en X (entre 1 et 3) :"))
    Colonne = int(input("Joueur 1 (X): Entrez la coordonnée en Y (entre 1 et 3) :"))
    

    #Vérifie si les coordonnées sont bonne (pas strictement inférieur à 1 et pas strictement supérieur à 3)
    while((Colonne < 1 or Colonne > 3) or (Ligne < 1 or Ligne > 3)):
        #Vérifie si le problème viens des coordonnées de la colonne
        if(Colonne < 1 or Colonne > 3):
            print("Vous avez entrée une coordonnée en Ligne incorrect !")
            Colonne = int(input("Entrez à nouveau une coordonnée de la colonne (compris entre 1 et 3): "))
            #Ou si le problème viens des lignes
        elif(Ligne < 1 or Ligne > 3):
            print("Vous avez entrée une coordonnée en Colonne incorrect !")
            Ligne = int(input("Entrez à nouveau une coordonnée de la ligne (compris entre 1 et 3): "))

    #Envois dans la fonction pour placer le pion du joueur sur la case entrée par le joueur
    JeuJoueur1(Colonne, Ligne, Tableau)

#Fonction pour placer le pion du joueur 1 là où à été demandé par le joueur 1 
def JeuJoueur1(Colonne : int, Ligne : int, Tableau : list[list[str]]) -> list[list[str]]:
    """
    Fonction qui place le point du joueur1 
    ENTREE : la colonne choisi, la ligne choisi, le tableau du morpion
    SORTIE : le tableau avec la case choisis rempli
    """
    #Vérifie si la case et vide
    system('cls' if name == 'nt' else 'clear')
    if (Tableau[Colonne - 1][Ligne - 1] == " "):
        #Si elle est vide, alors le programme place le pion du joueur 1
        Tableau[Colonne - 1][Ligne - 1] = "X"
    
    else :
        #Sinon si la case est déjà occupé, alors on lui dit qu'elle est déjà occupé
        system('cls' if name == 'nt' else 'clear')
        print("La ligne est déjà occupé !")
        #Et on lui redemande d'entrer à nouveau des coordonnées
        Joueur1(Tableau)
    
    #Il retourne "Tableau" pour ensuite l'enregistrer en général
    return Tableau
       
#Jeu du joueur 2
def Joueur2(Tableau : list[list[str]]) :
    """
    Procédure permettant au joueur1 de choisir où placer son point
    ENTREE : le tableau du morpion
    SORTIE : RIEN
    """
    Colonne : int
    Ligne : int

    print("Joueur 2 (O), à vous de jouer, entrez les coordonnées X (ligne) et Y (colonne) entre 1 et 3")
    Ligne = int(input("Joueur 2 (O): Entrez la coordonnée en X (entre 1 et 3) :"))
    Colonne = int(input("Joueur 2 (O): Entrez la coordonnée en Y (entre 1 et 3) :"))
    

    while((Colonne < 1 or Colonne > 3) or (Ligne < 1 or Ligne > 3)):
        if(Colonne < 1 or Colonne > 3):
            print("Vous avez entrée une coordonnée en Ligne incorrect !")
            Colonne = int(input("Entrez à nouveau une coordonnée de la colonne (compris entre 1 et 3): "))
        elif(Ligne < 1 or Ligne > 3):
            print("Vous avez entrée une coordonnée en Colonne incorrect !")
            Ligne = int(input("Entrez à nouveau une coordonnée de la ligne (compris entre 1 et 3): "))
    JeuJoueur2(Colonne, Ligne, Tableau)


def JeuJoueur2(Colonne : int, Ligne : int, Tableau : list[list[str]]) -> list[list[str]]:
    """
    Fonction qui place le point du joueur2 
    ENTREE : la colonne choisi, la ligne choisi, le tableau du morpion
    SORTIE : le tableau avec la case choisis rempli
    """
    system('cls' if name == 'nt' else 'clear')
    if (Tableau[Colonne - 1][Ligne - 1] == " "):
        Tableau[Colonne - 1][Ligne - 1] = "O"
    
    else :
        system('cls' if name == 'nt' else 'clear')
        print("La ligne est déjà occupé !")
        Joueur2(Tableau)
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

def Jeu_Morpion() -> None :
    """
    Procédure faisant tourner le jeu du morpion
    ENTREE : RIEN
    SORTIE : RIEN
    """
    joueurgagne : bool
    joueurgagne = False

    system('cls' if name == 'nt' else 'clear')
    Tableau : list[list[str]] 
    Tableau = TableauVide()
    
    #Boucle while du tant que un joueur n'a pas gagné, on reste dedans
    while(not joueurgagne):
        #Double vérification pour éviter de faire jouer les deux joueurs quand un à gagné
        
        if(joueurgagne == False):
            #Fonction pour faire jouer le joueur 1
            Joueur1(Tableau)
            #Affichage du tableau pour montrer où le joueur à placé son pion
            AfficherTableau(Tableau)
            #Fonction pour vérifier si le joueur à gagné
            joueurgagne = VerifierGagne(Tableau)

            if (joueurgagne):
                print("Le joueur 1 à gagné la partie !")
                print("Le joueur 2 à perdu !")
                
            if(joueurgagne == False):
                Joueur2(Tableau) 
                AfficherTableau(Tableau)
                joueurgagne = VerifierGagne(Tableau)

                if (joueurgagne == True):
                    print("Le joueur 2 à gagné la partie !")
                    print("Le joueur 1 à perdu !")

    return None