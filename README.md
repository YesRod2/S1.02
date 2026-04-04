# 🎮 Collection de Jeux Python

Une application console regroupant trois jeux classiques en Python, avec système de gestion des joueurs et sauvegarde des scores.

## 📋 Jeux Disponible

### 1. 🔢 La Devinette
- Le joueur 1 choisit un nombre entre 1 et 100
- Le joueur 2 doit le deviner en 10 essais maximum
- Indices : "trop grand" ou "trop petit"
- Mode ordinateur avec difficulté aléatoire ou intelligente

### 2. 🔥 Jeu des Allumettes
- 20 allumettes disposées en tas
- Chaque joueur retire 1, 2 ou 3 allumettes à son tour
- Celui qui prend la dernière allumette a perdu
- IA intelligente avec stratégie optimale

### 3. ❌ Morpion (Tic-Tac-Toe)
- Grille 3x3 classique
- Deux joueurs placent X et O tour à tour
- Premier à aligner 3 symboles gagne
- Support pour joueurs humains et ordinateurs

## 🚀 Fonctionnalités

- **Gestion des Joueurs** : Ajout et suivi des joueurs
- **Classements** : Scores séparés par jeu avec tri par ordre décroissant
- **Sauvegarde** : Persistance des données dans un fichier binaire (`sauvegarde.bin`)
- **Modes de Jeu** :
  - Joueur vs Joueur
  - Joueur vs Ordinateur (aléatoire ou intelligent)
  - Ordinateur vs Ordinateur
- **Interface Console** : Affichage coloré grâce au module `bcolors`
- **Multi-plateforme** : Compatible Windows, Linux et macOS
