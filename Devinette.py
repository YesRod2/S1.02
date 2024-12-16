from os import system, name
from bcolors import bcolors


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
    print("- Le joueur1 choisis un nombre entre 1 et 100.")
    print("- Le joueur2 doit alors devinier ce nombre en 10 essais sinon il a perdu.")
    print("- A chaque proposition du joueur2, le joueur1 répond -trop petit- ou -trop grand-")
    print()
    print(bcolors.bleu + "Appuyer sur entrer pour continuer.")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    print(bcolors.cyan + "------------------------------------------------------------------------------------------")
    return None

def Jeu_Devinette() -> bool:
    """
    Procédure permettant de joueur à la Devinette
    Entrée : RIEN
    Sortie : un booléen pour donner le résultat 
    """

    choix_joueur1 : int
    choix_joueur2 : int
    joueur1 : str
    essai : int
    nombre_essai : int

    essai = 9
    nombre_essai = 1

    system('cls' if name == 'nt' else 'clear')
    choix_joueur1 = int(input(bcolors.blanc + bcolors.cyan + "Joueur1, Choisissez un nombre entre " + bcolors.blanc + "1 " + bcolors.cyan + "et " + bcolors.blanc + "100" + bcolors.cyan + " : " + bcolors.blanc))   #le joueur1 choisis le nombre que le joueur2 doit trouver
    while choix_joueur1 > 100 or choix_joueur1 < 1 :   #fiabilisation pour respecter les règles du jeu
        choix_joueur1 = int(input(bcolors.rouge + "Vous avez dépassé la limite choisis, veuillez de nouveau donner un nombre : " + bcolors.blanc))
    system('cls' if name == 'nt' else 'clear')


    print(bcolors.blanc + bcolors.cyan + "Le joueur1 a choisis son nombre.")
    print("À vous de jouer joueur2, trouvez son nombre le plus vite possible.")
    choix_joueur2 = int(input("Quelle est votre nombre : " + bcolors.blanc))   #choix du premier nombre du joueur2
    while choix_joueur2 > 100 or choix_joueur2 < 1 :   #fiabilisation pour respecter les règles du jeu
        print(bcolors.rouge + "Pour rappel, le nombre choisis est entre " + bcolors.blanc + "1 " + bcolors.rouge + "et " + bcolors.blanc +"100" + bcolors.rouge + ": " + bcolors.blanc)
        choix_joueur2 = int(input(bcolors.cyan + "Votre nombre : " + bcolors.blanc))


    while choix_joueur2 != choix_joueur1 and essai != 0 :   #boucle "tant que" permettant de faire tourner le jeu, jusqu'à ce que le joueur2 trouve le bon nombre ou qu'il ai épuisé ses 10 essais 
        system('cls' if name == 'nt' else 'clear')
        print(bcolors.blanc + bcolors.cyan + "Le joueur2 à choisis se nombre :" + bcolors.blanc ,choix_joueur2)
        print(bcolors.blanc + bcolors.cyan + "Joueur1, le nombre choisis est-il trop grand ou trop petit ?")
        joueur1 = input("dîtes nous : " + bcolors.blanc)    #le joueur1 nous dis si le nombre est trop grand ou trop petit
        while joueur1 != "trop grand" and joueur1 != "trop petit":  #fiabilisation pour bien écrire
            print(bcolors.rouge + "Veillez à bien ortographié " + bcolors.blanc + "'trop grand / trop petit' " + bcolors.rouge + "s'il vous plait.")
            joueur1 = input(bcolors.blanc + bcolors.cyan + "Alors ? trop grand ou trop petit ? : " + bcolors.blanc)
        system('cls' if name == 'nt' else 'clear')


        if joueur1 == "trop grand":    #condition si/sinon qui enlève 1 essai et qui en fonction de 'trop grand' ou 'trop petit' écrit un message différent
            essai -= 1
            nombre_essai += 1
            choix_joueur2 = int(input(bcolors.blanc + bcolors.cyan + "Joueur2, votre nombre est trop grand, donnez-en un nouveau : " + bcolors.blanc))  #le joueur2 rechoisis donc un nombre
        else :
            essai -= 1
            nombre_essai += 1
            choix_joueur2 = int(input(bcolors.blanc + bcolors.cyan + "Joueur2, votre nombre est trop petit, donnez-en un nouveau : " + bcolors.blanc))  #le joueur2 rechoisis donc un nombre


    system('cls' if name == 'nt' else 'clear')
    if essai == 0 and choix_joueur2 != choix_joueur1  :    #condition si/sinon pour savoir si le joueur2 a gagné ou perdu
        print(bcolors.blanc + bcolors.cyan + "Vous avez utilisé vos 10 essais, ce qui veut dire que vous avez malheureusement"+ bcolors.rouge + " perdu" + bcolors.blanc + bcolors.cyan + ". Vous gagnerez la prochaine fois ! ")
        
        return True
    else:
        print(bcolors.cyan + "Bravo vous avez" + bcolors.blanc + bcolors.vert + " gagnez"  + bcolors.blanc + bcolors.cyan + ", vous avez trouvé le nombre du joueur1 en" + bcolors.blanc, nombre_essai, bcolors.cyan + "essais")
    
    return False