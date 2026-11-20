from os import system, name
from bcolors import bcolors
from random import randint
from time import sleep


def Regle_Devinette() -> None:
    """
    Procédure expliquant les règles de la devinette.
    Entrée : RIEN
    Sortie : RIEN
    """
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.jaune + "                     Règle du Jeu :")
    print("- Ce jeu se joue à 2 joueurs.")
    print("- Le joueur1 choisit un nombre entre 1 et 100.")
    print("- Le joueur2 doit alors deviner ce nombre en 10 essais sinon il a perdu.")
    print("- A chaque proposition du joueur2, le joueur1 répond -trop petit- ou -trop grand-")
    print()
    print(bcolors.bleu + "Appuyer sur entrer pour continuer.")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    return None

def Jeu_Devinette(joueur1 : str, joueur2 : str, difficulte : int) -> bool:
    """
    Fonction permettant de joueur à la Devinette
    Entrée : 
        - `joueur1`, une chaîne, qui représente le nom d'utilisateur du joueur 1.
        - `joueur2`, une chaîne, qui représente le nom d'utilisateur du joueur 2.
        - `difficulte`, un entier, qui représente la difficulté du joueur 2 si il est la machine.
    Sortie : un booléen, True si le joueur 1 gagne (le joueur 2 n'a pas trouvé en 10 essais), False si le joueur 2 gagne
    """

    choix_joueur1 : int
    choix_joueur2 : int
    phrase : str
    essai : int
    nombre_essai : int
    min : int
    max : int

    essai = 9
    nombre_essai = 1
    min = 1
    max = 100

    system('cls' if name == 'nt' else 'clear')

    #On regarde si le joueur 1 est un ordinateur ou un joueur
    if joueur1 == "Ordinateur1":
        choix_joueur1 = randint(1, 100)

    else:
        choix_joueur1 = int(input(f"{bcolors.blanc}{bcolors.cyan}{joueur1}, Choisissez un nombre entre {bcolors.blanc}1 {bcolors.cyan}et {bcolors.blanc}100{bcolors.cyan} : {bcolors.blanc}"))   #le joueur1 choisis le nombre que le joueur2 doit trouver
        while choix_joueur1 > 100 or choix_joueur1 < 1 :   #fiabilisation pour respecter les règles du jeu
            choix_joueur1 = int(input(bcolors.rouge + "Vous avez dépassé la limite choisis, veuillez de nouveau donner un nombre : " + bcolors.blanc))
    system('cls' if name == 'nt' else 'clear')


    print(f"{bcolors.blanc}{bcolors.cyan}{joueur1} a choisis son nombre.")
    print(f"À vous de jouer {joueur2}, trouvez son nombre le plus vite possible.")

    # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
    #sinon le joueur joue
    if joueur2 == "Ordinateur2":

        #On attends 2 secondes pour que l'utilisateur puisse lire le message
        sleep(2)

        #On regarde si l'ordinateur est intelligent ou non (1 = non intelligent, 2 = intelligent)
        if difficulte == 1:
            choix_joueur2 = randint(1, 100)
        else:
            choix_joueur2 = (min + max) // 2

    else:

        choix_joueur2 = int(input("Quel est votre nombre : " + bcolors.blanc))   #choix du premier nombre du joueur2
        while choix_joueur2 > 100 or choix_joueur2 < 1 :   #fiabilisation pour respecter les règles du jeu
            print(bcolors.rouge + "Pour rappel, le nombre choisis est entre " + bcolors.blanc + "1 " + bcolors.rouge + "et " + bcolors.blanc +"100" + bcolors.rouge + ": " + bcolors.blanc)
            choix_joueur2 = int(input(bcolors.cyan + "Votre nombre : " + bcolors.blanc))

    #boucle "tant que" permettant de faire tourner le jeu, jusqu'à ce que le joueur2 trouve le bon nombre ou qu'il ai épuisé ses 10 essais 
    while choix_joueur2 != choix_joueur1 and essai != 0 :   
        system('cls' if name == 'nt' else 'clear')
        
        print(f"{bcolors.blanc}{bcolors.cyan}{joueur2} a choisi ce nombre : {bcolors.blanc}{choix_joueur2}")
        print(f"{bcolors.blanc}{bcolors.cyan}{joueur1}, le nombre choisi est-il trop grand ou trop petit ?")

        # Si c'est un robot qui joue, un algorithme est donc lancé pour effectuer le tour du robot
        #sinon le joueur joue
        if joueur1 == "Ordinateur1":

            #On attends 2 secondes pour que l'utilisateur puisse lire le message
            sleep(2)

            if choix_joueur2 < choix_joueur1:
                print(f"{bcolors.blanc}{bcolors.cyan}trop petit")
                phrase = "trop petit"

                #On attends 2 secondes pour que l'utilisateur puisse lire le message
                sleep(2)

            else:
                print(f"{bcolors.blanc}{bcolors.cyan}trop grand")
                phrase = "trop grand"
                
                #On attends 2 secondes pour que l'utilisateur puisse lire le message
                sleep(2)

        else:

            phrase = input("dîtes-nous : " + bcolors.blanc).strip().lower()    #le joueur1 nous dit si le nombre est trop grand ou trop petit
            while phrase != "trop grand" and phrase != "trop petit":  #fiabilisation pour bien écrire
                print(bcolors.rouge + "Veillez à bien orthographier " + bcolors.blanc + "`trop grand / trop petit` " + bcolors.rouge + "s'il vous plaît.")
                phrase = input(bcolors.blanc + bcolors.cyan + "Alors ? trop grand ou trop petit ? : " + bcolors.blanc).strip().lower()

            #fiabilisation pour empêcher le joueur1 de se tromper ou de tricher
            while (phrase == "trop grand" and choix_joueur2 < choix_joueur1) or (phrase == "trop petit" and choix_joueur2 > choix_joueur1):
                print(f"{bcolors.rouge}Ce n'est pas vrai, votre nombre est {bcolors.blanc}{choix_joueur1}{bcolors.rouge} !")
                phrase = input(bcolors.blanc + bcolors.cyan + "Alors ? trop grand ou trop petit ? : " + bcolors.blanc).strip().lower()
        system('cls' if name == 'nt' else 'clear')


        if phrase == "trop grand":    #condition si/sinon qui enlève 1 essai et qui en fonction de 'trop grand' ou 'trop petit' écrit un message différent
            essai -= 1
            nombre_essai += 1

            if joueur2 == "Ordinateur2":
                #Le nombre est trop grand : le nombre cherché est forcément plus petit
                max = choix_joueur2 - 1

                #On regarde si le joueur 2 est un ordinateur intelligent ou non (1 = non intelligent, 2 = intelligent)
                if difficulte == 1:
                    choix_joueur2 = randint(min, max)   #au hasard, mais en tenant compte des indices

                else:
                    choix_joueur2 = (min + max) // 2   #recherche par dichotomie : on prend le milieu

            else:
                choix_joueur2 = int(input(f"{bcolors.blanc}{bcolors.cyan}{joueur2}, votre nombre est trop grand, donnez-en un nouveau : {bcolors.blanc}"))  #le joueur2 rechoisit donc un nombre
                while choix_joueur2 > 100 or choix_joueur2 < 1 :   #fiabilisation pour respecter les règles du jeu
                    choix_joueur2 = int(input(f"{bcolors.rouge}Le nombre doit être entre {bcolors.blanc}1{bcolors.rouge} et {bcolors.blanc}100{bcolors.rouge} : {bcolors.blanc}"))
        
        else:
            essai -= 1
            nombre_essai += 1

            if joueur2 == "Ordinateur2":
                #Le nombre est trop petit : le nombre cherché est forcément plus grand
                min = choix_joueur2 + 1

                #On regarde si le joueur 2 est un ordinateur intelligent ou non (1 = non intelligent, 2 = intelligent)
                if difficulte == 1:
                    choix_joueur2 = randint(min, max)   #au hasard, mais en tenant compte des indices

                else:
                    choix_joueur2 = (min + max) // 2   #recherche par dichotomie : on prend le milieu
            else:
                choix_joueur2 = int(input(f"{bcolors.blanc}{bcolors.cyan}{joueur2}, votre nombre est trop petit, donnez-en un nouveau : {bcolors.blanc}"))  #le joueur2 rechoisit donc un nombre
                while choix_joueur2 > 100 or choix_joueur2 < 1 :   #fiabilisation pour respecter les règles du jeu
                    choix_joueur2 = int(input(f"{bcolors.rouge}Le nombre doit être entre {bcolors.blanc}1{bcolors.rouge} et {bcolors.blanc}100{bcolors.rouge} : {bcolors.blanc}"))


    system('cls' if name == 'nt' else 'clear')

    #On regarde si les joueurs sont des ordinateurs ou des joueurs, pour écrire un message différent en fonction des joueurs ou ordinateurs
    if joueur1 != "Ordinateur1" and joueur2 != "Ordinateur2":
        if essai == 0 and choix_joueur2 != choix_joueur1:    #condition si/sinon pour savoir si le joueur2 a gagné ou perdu
            print(f"{bcolors.blanc}{bcolors.cyan}{joueur2}, vous avez utilisé vos 10 essais, ce qui veut dire que vous avez malheureusement{bcolors.rouge} perdu{bcolors.blanc}{bcolors.cyan}. Vous gagnerez la prochaine fois ! ")
        
        else:
            print(f"{bcolors.cyan}Bravo vous avez {bcolors.blanc}{bcolors.vert}gagné{bcolors.blanc}{bcolors.cyan}, vous avez trouvé le nombre de {joueur1} en {bcolors.blanc}{nombre_essai} {bcolors.cyan} essais")
    
    else:

        #Un message différent est écrit en fonction des joueurs ou ordinateurs

        if joueur1 == "Ordinateur1" and joueur2 != "Ordinateur2":

            if essai == 0 and choix_joueur2 != choix_joueur1:
                print(f"{bcolors.blanc}{bcolors.cyan}{joueur2}, vous avez utilisé vos 10 essais, ce qui veut dire que vous avez malheureusement{bcolors.rouge} perdu{bcolors.blanc}{bcolors.cyan}. Vous gagnerez la prochaine fois ! ")
            
            else:
                print(f"{bcolors.cyan}Bravo vous avez {bcolors.blanc}{bcolors.vert}gagné{bcolors.blanc}{bcolors.cyan}, vous avez trouvé le nombre de l'{joueur1} en {bcolors.blanc}{nombre_essai}{bcolors.cyan} essais")
        
        elif joueur1 != "Ordinateur1" and joueur2 == "Ordinateur2":

            if essai == 0 and choix_joueur2 != choix_joueur1:
                print(f"{bcolors.blanc}{bcolors.cyan}{joueur1}, l'{joueur2} n'a pas trouvé votre nombre en 10 essais, ce qui veut dire qu'il a malheureusement{bcolors.rouge} perdu{bcolors.blanc}{bcolors.cyan}. Bravo à vous {joueur1} ! ")
            
            else:
                print(f"{bcolors.cyan}L'{joueur2} a {bcolors.blanc}{bcolors.vert}gagné {bcolors.blanc}{bcolors.cyan}car il a trouvé le nombre de {joueur1} en {bcolors.blanc}{nombre_essai}{bcolors.cyan} essais")

        else:

            if essai == 0 and choix_joueur2 != choix_joueur1:
                print(f"L'{joueur1} a {bcolors.vert}gagné.")
            else:
                print(f"L'{joueur2} a {bcolors.vert}gagné.")
    
    #True si le joueur 1 gagne (le joueur 2 n'a pas trouvé), False si le joueur 2 gagne
    return essai == 0 and choix_joueur2 != choix_joueur1