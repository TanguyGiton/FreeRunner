import random
import os
import pickle
from tkinter import*


def recupscores():
    file_scores = open("scores.tkv2","rb")
    scores = pickle.load(file_scores)
    file_scores.close()
    return scores


def enregscore(scores):
    file_scores = open("scores.tkv2","wb")
    pickle.dump(scores,file_scores)
    file_scores.close()


def trierliste(liste,liste2):
    n = len(liste)
    for j in range(n-1):
        indicemax = j
        for k in range(j+1,n):
            if liste[k] > liste[indicemax]:
                indicemax = k
        if j != indicemax:
            liste[j] , liste[indicemax] = liste[indicemax] , liste[j]
            liste2[j] , liste2[indicemax] = liste2[indicemax] , liste2[j]

    return(liste,liste2)


def bestscore(score_player, pseudo_player):

    tableau_scores = recupscores()

    tableau_scores[0].append(score_player)
    tableau_scores[1].append(pseudo_player)


    trierliste(tableau_scores[0],tableau_scores[1])

    while len(tableau_scores[0]) > 10:
        valeur1 = tableau_scores[0][-1]
        tableau_scores[0].remove(valeur1)

        valeur2 = tableau_scores[1][-1]
        tableau_scores[1].remove(valeur2)

    enregscore(tableau_scores)

def affich_scores():
    scores = recupscores()
    trierliste(scores[0],scores[1])
    enregscore(scores)

    fenetre_scores=Toplevel()
    fenetre_scores.title("Scores")
    fenetre_scores.resizable(width=False, height=False)
    can = Canvas(fenetre_scores, height=250, width=250)
    can.grid(rowspan=15, columnspan=2)
    titre=Label(fenetre_scores,text="MEILLEURS SCORES",font=("Impact", 16))
    titre.grid(row=1,columnspan=2)

    pseudo = Label(fenetre_scores,text="PSEUDOS",font=("Arial", 14))
    pseudo.grid(row=2,column = 0)

    score = Label(fenetre_scores,text="SCORES",font=("Arial", 14))
    score.grid(row=2,column = 1)

    i = 0
    hauteur = 4
    for element in scores[1]:
        pseudo = Label(fenetre_scores,text=element,font=("Arial", 12))
        pseudo.grid(row=hauteur,column = 0)

        score = Label(fenetre_scores,text=str(round(scores[0][i]/100,1))+" m",font=("Arial", 12))
        score.grid(row=hauteur,column = 1)

        i+=1
        hauteur+=1

    fermer=Button(fenetre_scores,text="Fermer",command=fenetre_scores.destroy) #creation widget pour quitter scores
    fermer.grid(row=16,columnspan=2)

    fenetre_scores.update()

    fenetre_scores.mainloop()



def score_jeu(score_joueur):
    global nv_score, score_player, entre_pseudo
    score_player = score_joueur
    scores = recupscores()
    trierliste(scores[0],scores[1])
    enregscore(scores)

    if score_joueur > scores[0][-1] :
        nv_score=Toplevel()
        nv_score.title("Nouveau Meilleur Score")
        nv_score.resizable(width=False, height=False)

        place_score = 0
        while score_joueur < scores[0][place_score] :
            place_score += 1

        can = Canvas(nv_score, height=300, width=300)
        can.grid(rowspan = 15,columnspan=2)

        titre=Label(nv_score,text="NOUVEAU MEILLEUR SCORE",font=("Impact", 16))
        titre.grid(row=0,columnspan=2)

        sous_titre=Label(nv_score,text="Bravo, tu atteints la place N°"+str(place_score+1)+" dans le classement !",font=("Arial", 12))
        sous_titre.grid(row=1,columnspan=2)

        pseudo = Label(nv_score,text="PSEUDOS",font=("Arial", 13))
        pseudo.grid(row=3,column = 0)

        score = Label(nv_score,text="SCORES",font=("Arial", 13))
        score.grid(row=3,column = 1)

        i = 0
        hauteur = 4
        non_affich = True
        for element in scores[1]:
            if i == place_score and non_affich:
                entre_pseudo=Entry(nv_score,textvariable="Ton Pseudo")
                entre_pseudo.grid(row=hauteur,column = 0)
                entre_pseudo.focus()

                score = Label(nv_score,text=str(round(score_joueur/100,1))+" m",font=("Arial", 12,"bold"))
                score.grid(row=hauteur,column = 1)

                non_affich = False

            else :
                pseudo = Label(nv_score,text=scores[1][i],font=("Arial", 12))
                pseudo.grid(row=hauteur,column = 0)

                score = Label(nv_score,text=str(round(scores[0][i]/100,1))+" m",font=("Arial", 12))
                score.grid(row=hauteur,column = 1)
                i+=1

            hauteur+=1

        valide=Button(nv_score,text="Valider",command=valider)
        valide.grid(row=17,columnspan=2)

        nv_score.mainloop()

def valider():
    global nv_score, score_player
    pseudo_joueur=entre_pseudo.get()
    bestscore(score_player, pseudo_joueur)
    nv_score.destroy()






