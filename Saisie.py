from bcolors import bcolors


def Saisir_Entier(message : str) -> int:
    """
    Fonction qui demande un nombre entier à l'utilisateur,
    et qui redemande tant que la saisie n'est pas un nombre entier.
    ENTREE : `message`, une chaîne, le texte affiché pour demander le nombre
    SORTIE : le nombre entier saisi
    """
    nombre : int
    valide : bool

    nombre = 0
    valide = False

    #fiabilisation : tant que la saisie n'est pas un nombre entier, on redemande
    while not valide:
        try:
            nombre = int(input(message))
            valide = True
        except ValueError:
            #int() échoue si on tape une lettre, rien du tout, "2.5", etc.
            print(bcolors.rouge + "Vous devez entrer un nombre entier !" + bcolors.blanc)

    return nombre
