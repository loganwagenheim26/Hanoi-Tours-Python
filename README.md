
# 🕹️ Projet : Les Tours de Hanoï en Python (Interface Turtle)



https://github.com/user-attachments/assets/f5519777-726f-4d93-b294-84b9d39dcc0a


Ce projet a été réalisé dans le cadre du cursus universitaire **INF101**. Il s'agit d'une adaptation interactive et graphique du célèbre jeu de réflexion des **Tours de Hanoï**, développée entièrement en **Python** avec le module graphique **Turtle**.

## 📝 Présentation du jeu
Les Tours de Hanoï sont un jeu de réflexion composé de trois tiges (ou tours) et de plusieurs disques de diamètres différents. 
Le but du jeu est de déplacer la pile de disques de la tour de gauche (départ) vers la tour de droite (arrivée) en un minimum de coups, tout en respectant deux règles simples :
1. On ne peut déplacer qu'un seul disque à la fois (le plus haut d'une pile).
2. On ne peut jamais placer un disque sur un disque plus petit que lui.


## 🛠️ Fonctionnalités du projet

### 🔹 Partie Logique & Algorithmique
* **Initialisation dynamique :** Le jeu s'adapte au nombre de disques choisi par l'utilisateur au lancement.
* **Structure de données rigoureuse :** Modélisation de l'état des tours sous forme de listes imbriquées (`[[disques], [disques], [disques]]`).
* **Filtres de saisie robustes :** Gestion des erreurs de frappe utilisateur, interdiction des coups illégaux (disque plus grand posé sur un plus petit) ou tentatives de sélection sur des tours vides.
* **Option d'abandon :** Possibilité de quitter la partie à tout moment en tapant `-1` avec demande de confirmation.

### 🔹 Partie Graphique (Module Turtle)
* **Rendu personnalisé :** Plateau de jeu et tiges modélisés en bois (couleur marron).
* **Code couleur dynamique :** Chaque disque possède une couleur unique attribuée automatiquement selon son diamètre pour une meilleure lisibilité.
* **Animation en temps réel :** Rafraîchissement graphique fluide lors du déplacement des disques d'une tour à une autre.



## 📂 Structure du code

Le projet respecte les principes de la programmation structurée et de la modularité à travers deux fichiers principaux :
* 📄 **`Projet partieA,B,C.py`** : Contient le cœur algorithmique du programme (les fonctions de vérification, de gestion de la boucle de jeu et les interactions textuelles avec le joueur).
* 📄 **`turtel.py`** : Regroupe l'ensemble des fonctions graphiques dédiées au tracé du plateau, des tiges, des disques et à la mise à jour visuelle du jeu.



## 🚀 Comment lancer le projet ?

1. Assurez-vous d'avoir **Python** installé sur votre machine (idéalement via l'IDE **Spyder**).
2. Téléchargez les deux fichiers `Projet partieA,B,C.py` et `turtel.py` et placez-les impérativement **dans le même dossier**.
3. Ouvrez le fichier principal `Projet partieA,B,C.py` dans votre éditeur de code.
4. Exécutez le script (Touche `F5` sur Spyder).
5. Saisissez le nombre de disques souhaité dans la console et jouez !


## 👨‍💻 Auteurs
**Logan Wagenheim et** 
**Romain Garrigues**
