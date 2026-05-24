# -*- coding: utf-8 -*-

# PARTIE B: GRAPHISME AVEC TURTLE

import turtle
tortue = turtle.Turtle()
tortue.clear()
tortue.reset()
l= [[4], [3], [2,1]]
def dessinePlateau(n):
    # Initialisation de la fenêtre turtle
    fenetre = turtle.Screen()
    fenetre.setup(1000, 600)  # Définit la taille de la fenêtre
    fenetre.bgcolor("white")  # Définit la couleur de fond

    # Création de la tortue
    
    tortue.speed(0)  # Vitesse maximale de déplacement de la tortue

    # Paramètres du plateau
    epaisseur_plateau = 20
    epaisseur_tours = 6
    epaisseur_disque=20
    diametre_petit_disque = 40
    diam_dis=40+(n-1)*30
    increment_disques = 30
    ecart_tour = 20+(diam_dis)
    ecart_bord=20+(diam_dis/2)-3
    hauteur_tours = (n + 1) * epaisseur_disque
    longueur_plat=4*20+3*diam_dis

    
    #Remplissage marron fonctionnel avec l'objet tortue
    tortue.color("black", "brown")
    tortue.penup()
    tortue.goto(-400, -200)
    tortue.pendown()
    
    tortue.begin_fill()
    # On trace les 4 côtés du rectangle pour fermer la forme et valider le remplissage
    tortue.forward(longueur_plat)
    tortue.left(90)
    tortue.forward(epaisseur_plateau)
    tortue.left(90)
    tortue.forward(longueur_plat)
    tortue.left(90)
    tortue.forward(epaisseur_plateau)
    tortue.left(90)
    tortue.end_fill()
    
    #tours 1 
    tortue.color("black", "brown")
    tortue.begin_fill()
    tortue.penup()
    tortue.goto(-400+ecart_bord, -180)
    tortue.pendown()
    tortue.left(90)
    tortue.forward(hauteur_tours)
    tortue.right(90)
    tortue.forward(epaisseur_tours)
    tortue.right(90)
    tortue.forward(hauteur_tours)
    tortue.left(90)
    tortue.end_fill()
    
    #tours 2 
    tortue.color("black", "brown")
    tortue.begin_fill()
    tortue.penup()
    tortue.goto(-400+20+diam_dis+ecart_bord, -180)
    tortue.pendown()
    tortue.left(90)
    tortue.forward(hauteur_tours)
    tortue.right(90)
    tortue.forward(epaisseur_tours)
    tortue.right(90)
    tortue.forward(hauteur_tours)
    tortue.left(90)
    tortue.end_fill()
    
    #tours 3
    tortue.color("black", "brown")
    tortue.begin_fill()
    tortue.penup()
    tortue.goto(-400+longueur_plat-ecart_bord-3, -180)
    tortue.pendown()
    tortue.left(90)
    tortue.forward(hauteur_tours)
    tortue.right(90)
    tortue.forward(epaisseur_tours)
    tortue.right(90)
    tortue.forward(hauteur_tours)
    tortue.left(90)
    tortue.end_fill()
    
    
    
    
def disque(nd):
    diam_dis=40+(nd-1)*30
    epaisseur_disque=20
    tortue.forward(diam_dis)
    tortue.left(90)
    tortue.forward(epaisseur_disque)
    tortue.left(90)
    tortue.forward(diam_dis)
    tortue.left(90)
    tortue.forward(epaisseur_disque)
    tortue.left(90)
    
    

def dessine_disque(nd, plateau, n):
    """
    Cette fonction pour recevoir un numéro de disque, la configuration du plateau,
    et le nombre total de disques. Cette fonction trouve la position du disque nd sur le plateau, et le dessine aux bonnes
    coordonnées. Il faut donc calculer les coordonnées du disque en fonction des paramètres
    """
    m = ((n*30+10)/2)+20
    l = m*2-20
    a = (-400)+m
    h = a+l
    c = h+l
    i = 0
    
    #  Choix  d'une couleur dans la liste selon le numéro de disque (nd)
    couleurs = ["red", "blue", "yellow", "orange", "green", "purple"]
    couleur_disque = couleurs[(nd - 1) % len(couleurs)]
    turtle.color("black", couleur_disque)
    
    while i < len(plateau):
        if nd in plateau[i]:
            x = list(plateau[i]) #on prend la liste voulu dans plateau
            q = x.index(nd) #pposition de nd dans x (liste)
            z = -180+(q*20)#hauteur
            a = i
            diam_dis=40+(nd-1)*30
            if a == 0:
                turtle.up()
                turtle.goto(-377+15*(n-nd), z) #-377 car -400+20+3 (pour la moitié de l'épaisseur d'une tour et pour le bord)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()#colorer l'intérieur
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
            elif a == 1:
                turtle.up()
                turtle.goto(h-((40+(nd-1)*30)/2)+3, z)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
            elif a == 2:
                turtle.up()
                turtle.goto(c-((40+(nd-1)*30)/2)+3, z)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
        i += 1
    return

def efface_disque(nd, plateau, n):
    """
    Cette fonction pour recevoir un numéro de disque, la configuration du plateau,
    et le nombre total de disques. Cette fonction trouve la position du disque nd sur le plateau, et le dessine aux bonnes
    coordonnées. Il faut donc calculer les coordonnées du disque en fonction des paramètres
    """
    m = ((n*30+10)/2)+20
    l = m*2-20
    a = (-400)+m
    h = a+l
    c = h+l
    i = 0
    turtle.color("white", "white")
    while i < len(plateau):
        if nd in plateau[i]:
            x = list(plateau[i]) #on prend la liste voulu dans plateau
            q = x.index(nd) #pposition de nd dans x (liste)
            z = -180+(q*20)#hauteur
            a = i
            diam_dis=40+(nd-1)*30
            if a == 0:
                turtle.up()
                turtle.goto(-377+15*(n-nd), z) #-377 car -400+20+3 (pour la moitié de l'épaisseur d'une tour et pour le bord)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()#colorer l'intérieur
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
            elif a == 1:
                turtle.up()
                turtle.goto(h-((40+(nd-1)*30)/2)+3, z)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
            elif a == 2:
                turtle.up()
                turtle.goto(c-((40+(nd-1)*30)/2)+3, z)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
        i += 1
    dessinePlateau(n)
    un=1
    while un!=n+1:
        if un!=nd:
            dessine_disque(un,plateau,n)
        un=un+1
    return


def efface_disque2(nd, plateau, n):
    """
    Cette fonction pour recevoir un numéro de disque, la configuration du plateau,
    et le nombre total de disques. Cette fonction trouve la position du disque nd sur le plateau, et le dessine aux bonnes
    coordonnées. Il faut donc calculer les coordonnées du disque en fonction des paramètres
    """
    m = ((n*30+10)/2)+20
    l = m*2-20
    a = (-400)+m
    h = a+l
    c = h+l
    i = 0
    turtle.color("white", "white")
    while i < len(plateau):
        if nd in plateau[i]:
            x = list(plateau[i]) #on prend la liste voulu dans plateau
            q = x.index(nd) #pposition de nd dans x (liste)
            z = -180+(q*20)#hauteur
            a = i
            diam_dis=40+(nd-1)*30
            if a == 0:
                turtle.up()
                turtle.goto(-377+15*(n-nd), z) #-377 car -400+20+3 (pour la moitié de l'épaisseur d'une tour et pour le bord)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()#colorer l'intérieur
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
            elif a == 1:
                turtle.up()
                turtle.goto(h-((40+(nd-1)*30)/2)+3, z)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
            elif a == 2:
                turtle.up()
                turtle.goto(c-((40+(nd-1)*30)/2)+3, z)
                turtle.down()
                i = 1
                while i <= 2:
                    turtle.begin_fill()
                    turtle.forward(diam_dis)
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.left(90)
                    turtle.end_fill()
                    i += 1
        i += 1
    dessinePlateau(n)
    return


def effaceTout(plateau, n):
    i=1
    while i<n+1:
        efface_disque2(i, plateau, n)
        i=i+1

def dessineConfig(plateau, n):
    i=1
    while i<n+1:
        dessine_disque(i, plateau, n)
        i=i+1