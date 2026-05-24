# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:44:31 2023

@author: Wagenheim
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:44:31 2023

@author: Wagenheim
Project: Les Tours de Hanoï - Parties A, B et C
"""

import turtle
# Importation des fonctions graphiques depuis votre fichier turtel.py
from turtel import dessinePlateau, dessineConfig, dessine_disque, efface_disque


# PARTIE A : PLATEAU DE JEU ET LISTES


def init(n):
    """
    Renvoie la configuration initiale du plateau avec n disques empilés
    sur la tour de gauche (indice 0), les autres tours étant vides.
    """
    # Exemple pour n=3 : [[3, 2, 1], [], []]
    tour_gauche = list(range(n, 0, -1))
    return [tour_gauche, [], []]


def nbDisques(plateau, numtour):
    """
    Renvoie le nombre de disques présents sur la tour 'numtour'.
    """
    return len(plateau[numtour])


def disqueSup(plateau, numtour):
    """
    Renvoie le numéro du disque supérieur de la tour 'numtour'.
    Renvoie -1 si la tour est vide ou si l'indice est incorrect.
    """
    if numtour < 0 or numtour > 2 or len(plateau[numtour]) == 0:
        return -1
    return plateau[numtour][-1]


def posDisque(plateau, numdisque):
    """
    Renvoie le numéro de la tour (0, 1 ou 2) sur laquelle se trouve le disque.
    """
    for i in range(3):
        if numdisque in plateau[i]:
            return i
    return -1


def verifDepl(plateau, nt1, nt2):
    """
    Vérifie si le déplacement de la tour nt1 vers la tour nt2 est autorisé.
    """
    # Vérification des indices des tours
    if nt1 < 0 or nt1 > 2 or nt2 < 0 or nt2 > 2:
        return False
        
    disque_depart = disqueSup(plateau, nt1)
    
    # Si la tour de départ est vide, déplacement impossible
    if disque_depart == -1:
        return False
        
    disque_arrivee = disqueSup(plateau, nt2)
    
    # Si la tour d'arrivée est vide, ou si le disque à poser est plus petit
    if disque_arrivee == -1 or disque_depart < disque_arrivee:
        return True
        
    return False


def verifVictoire(plateau, n):
    """
    Vérifie si tous les n disques sont empilés sur la tour de droite (indice 2).
    """
    tour_gauche_vide = (len(plateau[0]) == 0)
    tour_milieu_vide = (len(plateau[1]) == 0)
    
    # La tour de droite doit contenir exactement la liste initiale attendue
    solution_attendue = list(range(n, 0, -1))
    tour_droite_gagnante = (plateau[2] == solution_attendue)
    
    return tour_gauche_vide and tour_milieu_vide and tour_droite_gagnante



# PARTIE C : INTERACTIONS AVEC LE JOUEUR


def lireCoords(plateau):
    """
    Demande et filtre les saisies de l'utilisateur pour la tour de départ 
    et la tour d'arrivée. Autorise -1 pour abandonner.
    """
    while True:
        # 1. Saisie de la tour de départ
        try:
            nt1 = int(input("Tour de départ? (0, 1, 2 ou -1 pour abandonner) : "))
        except ValueError:
            print("Invalide, veuillez entrer un entier.")
            continue
            
        if nt1 == -1:
            return -1, -1
            
        if nt1 < 0 or nt1 > 2:
            print("Invalide, la tour doit être entre 0 et 2.")
            continue
            
        if nbDisques(plateau, nt1) == 0:
            print("Invalide, tour vide.")
            continue
            
        # 2. Saisie de la tour d'arrivée
        try:
            nt2 = int(input("Tour d'arrivée? (0, 1, 2) : "))
        except ValueError:
            print("Invalide, veuillez entrer un entier.")
            # On redemande tout depuis le début pour éviter un blocage
            continue 
            
        if nt2 < 0 or nt2 > 2:
            print("Invalide, la tour doit être entre 0 et 2.")
            continue
            
        # Vérification de la validité du déplacement global
        if verifDepl(plateau, nt1, nt2):
            return nt1, nt2
        else:
            print("Invalide, vous ne pouvez pas placer un disque sur un disque plus petit.")


def jouerUnCoup(plateau, n):
    """
    Gère le déplacement d'un disque : demande les coordonnées, met à jour 
    le modèle de données (plateau) et l'affichage graphique.
    """
    nt1, nt2 = lireCoords(plateau)
    
    # Si le joueur a choisi l'abandon (-1)
    if nt1 == -1:
        return False
        
    disque_a_deplacer = disqueSup(plateau, nt1)
    
    # Mise à jour graphique : on efface le disque de l'ancienne tour
    efface_disque(disque_a_deplacer, plateau, n)
    
    # Mise à jour de la structure de données (la liste plateau)
    plateau[nt1].pop()
    plateau[nt2].append(disque_a_deplacer)
    
    # Mise à jour graphique : on redessine le disque sur sa nouvelle tour
    dessine_disque(disque_a_deplacer, plateau, n)
    
    print(f"Je déplace le disque {disque_a_deplacer} de la tour {nt1} à la tour {nt2}")
    return True


def boucleJeu(plateau, n):
    """
    Boucle principale qui gère le déroulement de la partie.
    """
    nb_coups = 0
    abandon = False
    
    while not verifVictoire(plateau, n):
        print(f"\nCoup numéro {nb_coups + 1}")
        
        # Exécute un coup. Si jouerUnCoup renvoie False, c'est que le joueur abandonne
        continuer = jouerUnCoup(plateau, n)
        
        if not continuer:
            confirmation = input("Tu souhaites abandonner (oui/non)? ").strip().lower()
            if confirmation == 'oui':
                abandon = True
                break
            else:
                continue # On ignore l'abandon et on poursuit
                
        nb_coups += 1
        
    if abandon:
        print(f"Abandon de la partie après {nb_coups} coups. Au-revoir.")
        return nb_coups, False
    else:
        print(f"\nFélicitations ! Victoire en {nb_coups} coups !")
        return nb_coups, True



# PROGRAMME PRINCIPAL (MAIN)


if __name__ == "__main__":
    print("Bienvenue dans les Tours de Hanoï")
    
    # Demande du nombre de disques
    n_disques = 0
    while n_disques <= 0:
        try:
            n_disques = int(input("Combien de disques? "))
            if n_disques <= 0:
                print("Le nombre de disques doit être supérieur à 0.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
            
    # Initialisation de la structure de données
    plateau = init(n_disques)
    
    # Initialisation graphique avec votre module turtel
    dessinePlateau(n_disques)
    dessineConfig(plateau, n_disques)
    
    # Lancement de la boucle de jeu
    coups_joues, a_gagne = boucleJeu(plateau, n_disques)
    
    # Calcul du nombre minimal théorique de coups : (2^n) - 1
    coup_min = (2 ** n_disques) - 1
    print(f"\n--- FIN DE LA PARTIE ---")
    print(f"Nombre de coups joués : {coups_joues}")
    print(f"Le nombre minimal de coups possible était : {coup_min}")
    
    # Garder la fenêtre de dessin ouverte
    turtle.done()