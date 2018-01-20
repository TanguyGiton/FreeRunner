from tkinter import*
import os
import random
import pickle
import time
import math
import projet
import module_scores

#fonctions commandees par bouttons

def regles():
    fenetre2=Toplevel() # ouverture d'une nouvelle fenetre
    fenetre2.title("R\xE8gles du Jeu") #titre de la fenetre = Regles du Jeu
    fenetre2.resizable(width=False, height=False) # ne peut pas changer la taille de la fenetre

    can2=Canvas(fenetre2,height=500,width=325) # dimension de la fenetre graphique (avec height=hauteur, width=largeur)
    photo2=PhotoImage(file="regles_du_jeu.gif") #insertion de l'image des regles
    item=can2.create_image(160,250,image=photo2) #placement de l'image aux pixels...
    can2.grid()  # composition de la fenetre graphique d'une grille par defaut
    fenetre2.mainloop() # lancement de la fenetre


def jouer():
    projet.show_jeu(True)
    # programme Tanguy + Valentin


#----------fenetre principale
fenetre=Tk()
fenetre.resizable(width=False, height=False)
fenetre.title("Menu Principal")

#-------------fond menu
can=Canvas(fenetre,height=500,width=300)
photo=PhotoImage(file="imagetest3.gif")# image qui est dans le meme repertoire que le script Python
item=can.create_image(150,250,image=photo) # placement de l'image aux pixels 150,250
can.grid(row=0,rowspan=1000,column=0) # grille de la fenetre graphique (avec row=ligne, rowspan=nb de lignes totales, column=colonne)


#-------widget button''let's go''
image_go=PhotoImage(file="go_button.gif")
but1=Button(fenetre,image=image_go,command=jouer) #va permettre de lancer le jeu
but1.grid(row=467,column=0)

#---------widget button "regles du jeu"
image_regles=PhotoImage(file="regles_button.gif")
but2=Button(fenetre,image=image_regles,command=regles) #va faire apparaitre une autre fenetre qui contient regles du jeu
but2.grid(row=598,column=0)

#-------widget button"scores"
image_scores=PhotoImage(file="scores_button.gif")
but3=Button(fenetre,text='Scores',image=image_scores,command=module_scores.affich_scores) #permet d'afficher les scores obtenus
but3.grid(row=737,column=0)

#------------creation widget "quitter"
image_quitter=PhotoImage(file="quitter_button.gif")
but4=Button(fenetre,text="Quitter",image=image_quitter,command=fenetre.destroy) #permet de fermer la fenetre
but4.grid()

#---------on lance le programme
fenetre.mainloop()