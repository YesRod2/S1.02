# Collection de Jeux Python

Une application console regroupant trois jeux classiques en Python, avec un système de gestion des joueurs et de sauvegarde des scores.

## Lancer l'application

**Prérequis :** Python 3.10 ou plus récent. Aucune bibliothèque externe n'est nécessaire.

Depuis le dossier du projet :

```bash
python Menu.py
```

Sous Linux ou macOS, la commande peut être `python3 Menu.py`.

## Jeux disponibles

### 1. La Devinette
- Le joueur 1 choisit un nombre entre 1 et 100.
- Le joueur 2 doit le deviner en 10 essais maximum.
- À chaque proposition, le joueur 1 répond « trop grand » ou « trop petit ». Une réponse fausse est refusée, il est donc impossible de tricher.
- Ordinateur aléatoire : propose un nombre au hasard, mais en tenant compte des indices déjà reçus.
- Ordinateur intelligent : recherche par dichotomie, il trouve toujours en 7 essais maximum.

### 2. Jeu des Allumettes
- 20 allumettes disposées en tas.
- Chaque joueur retire 1, 2 ou 3 allumettes à son tour.
- Celui qui doit prendre la dernière allumette a perdu : la partie s'arrête dès qu'il n'en reste plus qu'une.
- Ordinateur aléatoire : retire un nombre d'allumettes au hasard.
- Ordinateur intelligent : applique la stratégie optimale (laisser à l'adversaire un nombre d'allumettes de la forme 4k + 1).

### 3. Morpion (Tic-Tac-Toe)
- Grille 3x3 classique, le joueur 1 joue les X et le joueur 2 les O.
- On choisit sa case en donnant la ligne puis la colonne (entre 1 et 3).
- Le premier à aligner 3 symboles (ligne, colonne ou diagonale) gagne.
- Si la grille est pleine sans alignement, c'est un match nul.
- Ordinateur aléatoire : joue sur une case libre au hasard.
- Ordinateur intelligent : gagne s'il le peut, sinon bloque l'adversaire, sinon prend le centre, puis un coin.

## Fonctionnalités

- **Gestion des joueurs** : ajout de joueurs depuis le menu des joueurs. Un nom ne peut pas être vide, déjà utilisé, ni être « Ordinateur1 » ou « Ordinateur2 » (réservés aux ordinateurs).
- **Modes de jeu** :
  - Joueur contre Joueur
  - Joueur contre Ordinateur (aléatoire ou intelligent)
  - Ordinateur contre Ordinateur
- **Classements** : un classement par jeu, trié par score décroissant. Seules les parties entre deux joueurs humains rapportent des points (1 point par victoire, aucun en cas de match nul).
- **Sauvegarde** : les joueurs et leurs scores sont enregistrés dans le fichier binaire `sauvegarde.bin` en quittant l'application (choix 5 du menu principal), puis rechargés automatiquement au lancement suivant.
- **Saisies sécurisées** : toutes les saisies sont vérifiées. Une lettre à la place d'un nombre, un choix hors menu ou un identifiant de joueur inexistant sont refusés et la question est reposée.
- **Interface console** : affichage en couleur grâce au module `bcolors`.
- **Multi-plateforme** : fonctionne sous Windows, Linux et macOS. Sous Windows, il est conseillé d'utiliser le Terminal Windows ou PowerShell, car l'ancienne invite de commandes (`cmd`) peut mal afficher les couleurs.

## Utilisation

1. Au lancement, la sauvegarde est chargée si le fichier `sauvegarde.bin` existe.
2. Ouvrir le menu des joueurs (choix 1) pour ajouter des joueurs. Il en faut **au moins 2** pour accéder aux jeux.
3. Choisir un jeu, puis lire les règles ou lancer une partie.
4. Pour chaque joueur, indiquer s'il s'agit d'un ordinateur. Sinon, le choisir grâce à son identifiant affiché dans le classement.
5. Quitter avec le choix 5 pour sauvegarder les scores.

## Structure du projet

| Fichier | Rôle |
|---|---|
| `Menu.py` | Point d'entrée : menu principal, lancement des jeux, chargement et sauvegarde des scores |
| `Menu_Joueur.py` | Classe `Joueurs`, menu des joueurs, ajout et choix des joueurs, classements et tris |
| `Devinette.py` | Jeu de la Devinette |
| `Allumettes.py` | Jeu des Allumettes |
| `Morpion.py` | Jeu du Morpion |
| `Saisie.py` | Fonction `Saisir_Entier` qui redemande tant que la saisie n'est pas un nombre entier |
| `bcolors.py` | Codes couleur ANSI pour l'affichage dans la console |
