# ***** MODULES ***** #

# On importe les modules dont nous aurons besoin :

from tkinter import*            # Tkinter pour l'interface graphique
import os                       # OS pour definir le dossier de demarrage du jeu
import random                   # random pour obtenir un nombre au hasard
import pickle                   # Pickle pour enregistrer des données dans un fichier (scores)
import time                     # time pour interagir avec le temps
import math                     # math pour effectuer des calculs poussés (logarithme, sinus, ..)
import module_scores            # et on importe les fonctions du fichier module_scores.py






# ***** FONCTIONS ***** #



# ---- La fonction jeu appelle les differentes fonctions du jeu en boucle (elle s'appelle elle meme)

def jeu():                                      #                                             |      <---|
                                                #                                             |          |
    obstacle()                                  # Appelle la fonction obstacle                |          |
                                                #                                             |          |
    if cheat == False:                          # Si le cheat n'est pas active                |          |
        collision()                                 # Alors on appelle la fonction collision  |          |
                                                #                                             |          |
    action()                                    # Appelle la fonction action                  |          |
    images()                                    # Appelle la fonction images                  |          |
    scores()                                    # Appelle la fonction scores                  |          |
                                                #                                             |          |
    if mod_bonus:                               # Si le "mode bonus" est active               |          |
        bonus()                                     # Alors on appelle la fonction bonus      |          |
                                                #                                             |          |
    if go:                                      # Si le jeu n'est pas arrete                  |          |
        fenetre_jeu.after(vitesse,jeu)              # Alors appelle la fonction jeu          \/      ____|







# ---- fonction clavier, cette fonction est appele a chaque fois que l'utilisateur appuie sur une trouche du clavier

def action_clavier(event):

    global action_sauter, action_baisser, dx_obstacle                                           # On rend les variables
    global cheat, affich_hitbox, t_cheat, man, touche                                           # accessiblent par
    global cheat_bonus, mod_bonus                                                               # tout le programme
                                                                                                #
    touchec = event.char                                                                        # la variable touchec prend la valeur de
                                                                                                # la touche pressee par l'utilisateur
                                                                                                #
    if touchec == "z" and action_baisser == False:                                              # Si la touche est z et que le bonhomme ne se baisse pas
        action_sauter = True                                                                        # alors la variable action_sauter devient vrai
                                                                                                #
    elif touchec == "s" and action_sauter == False:                                             # Sinon si la touche est s et que le bonhomme ne saute pas
        action_baisser = True                                                                       # alors la variable action_baisse devient vrai
                                                                                                #
    elif touchec == "p" and go:                                                                 # Sinon si la touche est p et que le jeu tourne
        stop()                                                                                      # alors on appelle la fonction stop
                                                                                                #
    elif (touchec == "p" and go != True) or (touchec == "r" and touche == True) :               # Sinon si la touche est p et le jeu ne tourne pas ou la
                                                                                                # touche est r et qu'il y a eu collision
        start()                                                                                     # alors on appelle la fonction start
                                                                                                #
    elif touchec == "c" :                                                                       # Sinon si la touche est c
        if cheat:                                                                                   # Si le cheat actif
            cheat = False                                                                               # alors on désactive le cheat
            can_jeu.delete(t_cheat)                                                                     # et on supprime le texte
            t_cheat = can_jeu.create_text(5,5,text='',anchor="nw")                                      # affichant CHEAT !
                                                                                                #
        else :                                                                                      # Sinon (si le cheat est inactif)
            cheat = True                                                                                # alors on active le cheat
            can_jeu.delete(t_cheat)                                                                     # et on affiche le texte
            t_cheat = can_jeu.create_text(5,5,text='CHEAT !',anchor="nw")                               # CHEAT !
                                                                                                #
    elif touchec == "h":                                                                        # Sinon si la touche est h
        if affich_hitbox:                                                                           # Si la hitbox est affichee
            affich_hitbox = False                                                                       # alors la variable affich_hitbox devient faux
            can_jeu.delete(man)                                                                         # et on cache la hitbox
                                                                                                #
        else :                                                                                      # Sinon (si la hitbox est cachee)
            affich_hitbox = True                                                                        # alors la variable affich_hitbox devient vrai
            man = can_jeu.create_rectangle(x2,y2,x2+largeur_man,y2+hauteur_man,outline="red")           # et on affiche la hitbox
                                                                                                #
    elif touchec == "b":                                                                        # Sinon si la touche est b
        cheat_bonus = True                                                                          # alors on active le cheat bonus
                                                                                                #
    elif touchec == "m" :                                                                       # Sinon si la touche est m
        if mod_bonus:                                                                               # Si le mode bonus est active
            mod_bonus = False                                                                           # alors on désactive le mode bonus
        else:                                                                                       # Sinon (si le mode bonus est desactive)
            mod_bonus = True                                                                            # alors on active le mode bonus






# ---- fonction action qui appelle les fonctions en fonction de l'action a effectuer

def action():

    global action_sauter, action_baisser        # On rend la variable utilisable dans tous le programme
                                                #
    if action_sauter:                           # Si la variable action_sauter est vrai (touche z)
        sauter()                                    # alors on appelle la fonction sauter
    if action_baisser:                          # Si la variable action_baisser est vrai (touche s)
        baisser()                                   # alors on appelle la fonction baisser

#fonction scores

def scores():
    global x1, x2, largeur_obstacle, texte, score, dx_obstacle
    score += dx_obstacle
    can_jeu.itemconfigure(texte,text=str(round(score/100,1))+" m")
    if score > 0 and type_bonus != 2:
        dx_obstacle = int(math.log(score))

# fonction images qui s'occupe de l'animation du stick man

def images():
    global n_image, x2, y2, photo_man, compt_rafraich_image, rafraich_image, dx_obstacle, corr_x, corr_y, hauteur_man, photos, action_baisser, action_sauter
    global debut, longueur_saut, hauteur_saut, y2_o, xf, photo_f1, photo_f2
    global n_image_b
    can_jeu.coords(photo_f1, int(xf),0)
    can_jeu.coords(photo_f2, int(xf),0)
    xf -= math.log(dx_obstacle)/6
    if xf <= 0:
        xf = photo_fond.width()
    can_jeu.coords(photo_fond, x1,y2+hauteur_man-corr_y)
    if compt_rafraich_image > rafraich_image:
        compt_rafraich_image = 0
        if action_sauter != True and action_baisser != True:
            can_jeu.delete(photo_man)
            photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photos[n_image-1])
            n_image += 1
            if n_image > 6 :
                n_image = 1
        elif action_sauter:
            if y2 > (y2_o - hauteur_saut) and debut < longueur_saut:
                can_jeu.delete(photo_man)
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photo_saute1)
            elif debut >= longueur_saut  and y2 < y2_o:
                can_jeu.delete(photo_man)
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photo_saute3)
            else:
                can_jeu.delete(photo_man)
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photo_saute2)
        elif action_baisser:
            can_jeu.delete(photo_man)
            photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photos[n_image_b-1])
            n_image_b +=1
            if n_image_b>12:
                n_image_b=8
        if action_baisser == False and n_image_b != 6:
            can_jeu.delete(photo_man)
            photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photos[12])
            n_image_b = 6
    can_jeu.update()
    compt_rafraich_image += dx_obstacle
    if action_baisser:
        compt_rafraich_image = compt_rafraich_image - dx_obstacle + rafraich_image/2.5

# fonction obstacle qui g

def obstacle():
    global hauteur_obstacle, largeur_obstacle, hauteur_man, largeur_man,largeur_fenetre,hauteur_fenetre
    global x1, y1, dx_obstacle, dy_obstacle, vitesse

    x1, y1 = x1 - dx_obstacle, y1 - dy_obstacle
    nb_rand = random.randint(1,2)
    if x1<-largeur_obstacle:
        x1 = largeur_fenetre + largeur_obstacle
        y1 = hauteur_fenetre - (nb_rand*hauteur_obstacle)

    can_jeu.coords(carre1, x1, y1, x1+largeur_obstacle, y1+hauteur_obstacle)

# fonction collision
def collision():
    global x1, x2, largeur_man, largeur_obstacle, hauteur_man, hauteur_obstacle, y1, score, touche
    if x1<x2+largeur_man and x1>x2-largeur_obstacle and y1<y2+hauteur_man and y1>y2-hauteur_obstacle:
        print("Touche !")
        touche = True
        stop()

# fonction clic souris
def clic_souris(event):
    global coord_bonus_x, coord_bonus_y, cote_bonus, activ_bonus, chaine, cheat, type_bonus
    if activ_bonus:
        if event.x >= coord_bonus_x and event.x <= coord_bonus_x + cote_bonus and event.y >= coord_bonus_y and event.y <= coord_bonus_y + cote_bonus :
            coord_bonus_x = - cote_bonus

# fonction bonus
def bonus():
    global activ_bonus, coord_bonus_x, coord_bonus_y,cote_bonus, largeur_fenetre, ico_bonus,type_bonus, cheat_bonus, longueur_run, var_bonus, dx_obstacle, cheat
    if activ_bonus:
        coord_bonus_x -= 1
        coord_bonus_y = int(math.sin(coord_bonus_x*0.05)*20) + 25
        if coord_bonus_x <= -cote_bonus:
            coord_bonus_x = largeur_fenetre + cote_bonus
            activ_bonus = False
    elif type_bonus == 0 :
        chance = random.randint(1,1000)
        if chance == 43 or cheat_bonus:
            cheat_bonus = False
            type_bonus = random.randint(1,3)
            if type_bonus == 1 :
                couleur ="green"
            elif type_bonus == 2 :
                couleur = "blue"
            elif type_bonus == 3:
                couleur = "orange"
            can_jeu.itemconfigure(ico_bonus, fill = couleur)
            activ_bonus = True

    elif type_bonus == 1:
        cheat = True
        can_jeu.itemconfigure(chaine, text = "Bonus 1 actif")
        if x1<x2+largeur_man and x1>x2-largeur_obstacle and y1<y2+hauteur_man and y1>y2-hauteur_obstacle:
            if var_bonus == 0 :
                var_bonus = score + 100
            elif var_bonus <= score:
                type_bonus = 0
                var_bonus = 0
                cheat = False

    elif type_bonus == 2 :
        cheat = True
        can_jeu.itemconfigure(chaine, text = "Bonus 2 actif")
        if var_bonus < longueur_run*0.95:
            dx_obstacle = 20
        else :
            dx_obstacle = 7

        var_bonus += dx_obstacle

        if var_bonus >= longueur_run:
            var_bonus = 0
            type_bonus = 0
            cheat = False

    elif type_bonus == 3:
        can_jeu.itemconfigure(chaine, text = "Bonus 3 actif")
        type_bonus = 0

    can_jeu.coords(ico_bonus, coord_bonus_x, coord_bonus_y, coord_bonus_x+cote_bonus, coord_bonus_y+cote_bonus)
    can_jeu.update()





# fonction sauter
def sauter():
    global x2, y2, x2_o, y2_o, hauteur_man, largeur_man, hauteur_saut, action_sauter, debut, longueur_saut, corr_x, corr_y
    debut += 2 + int(dx_obstacle/10)
    if y2 > (y2_o - hauteur_saut) and debut < longueur_saut:
        y2 -= (hauteur_saut/3)
    elif debut >= longueur_saut  and y2 < y2_o:
        y2 += (hauteur_saut/3)
    elif y2 == y2_o :
        debut = 0
        action_sauter = False
    if affich_hitbox:
        can_jeu.coords(man, x2, y2, x2+largeur_man, y2+hauteur_man)
    can_jeu.coords(photo_man, x2+corr_x,y2+hauteur_man-corr_y)
    print("Saute !")

# fonction baisser
def baisser():
    global x2, y2, hauteur_man, largeur_man, hauteur_saut, action_baisser, debut, longueur_saut
    debut += 2 + int(dx_obstacle/10)
    if y2 != (y2_o + hauteur_man - largeur_man) and y2 != (y2_o +largeur_man - hauteur_man) and debut < longueur_saut+10:
        y2 = y2_o + hauteur_man - largeur_man
        hauteur_man, largeur_man = largeur_man, hauteur_man
    elif debut >= longueur_saut+10 and y2 != y2_o:
        y2 = y2_o
        hauteur_man, largeur_man = largeur_man, hauteur_man
    elif y2 == y2_o :
        debut = 0
        action_baisser = False
    if affich_hitbox:
        can_jeu.coords(man, x2, y2, x2+largeur_man, y2+hauteur_man)
    can_jeu.coords(photo_man, x2+corr_x,y2+hauteur_man-corr_y)
    print("Baisses !")

# fonction stop
def stop():
    global go
    if go:
        go = False
        arret()


# fonction arret
def arret():
    global go, alt_pose, photo_man, largeur_fenetre, x2, corr_x, y2, corr_y, hauteur_man, photo_pose1, photo_pose2, photos, hauteur_fenetre
    global n_image_b, photo_mort, t_sous_central
    if go != True:
        if touche:
            if y2+hauteur_man < hauteur_fenetre:
                y2 += 3
            if x2+corr_x < largeur_fenetre/2 :
                x2 += 3
                if x2%5 == 0 :
                    n_image_b +=1
                if n_image_b>12:
                    n_image_b=8
                can_jeu.delete(photo_man)
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photos[n_image_b])
            else :
                can_jeu.delete(photo_man)
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photo_mort)
                can_jeu.itemconfigure(t_central,text=texte_collision)
                can_jeu.itemconfigure(texte,text="")
                can_jeu.itemconfigure(t_sous_central,text="Score : "+str(round(score/100,1))+" m. Press R or P to retry")
                module_scores.score_jeu(score)
            fenetre_jeu.after(5,arret)
        else:
            can_jeu.itemconfigure(t_central,text=texte_pause)
            can_jeu.delete(photo_man)
            if alt_pose:
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photo_pose1)
                alt_pose = False
            else:
                photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photo_pose2)
                alt_pose = True
            can_jeu.update()

            fenetre_jeu.after(500,arret)


# fonction start
def start():
    global go, touche, restart
    if go==False:
        can_jeu.itemconfigure(t_central,text='')
        can_jeu.itemconfigure(t_sous_central,text='')
        go = True
        if touche:
            show_jeu(False)
        jeu()


def show_jeu(first):
    global go, action_baisser, action_sauter, cheat, affich_hitbox, largeur_fenetre, hauteur_fenetre, score, largeur_obstacle, hauteur_obstacle, t_sous_central
    global dx_obstacle, dy_obstacle, vitesse, x1, y1, hauteur_man, largeur_man, x2_o, y2_o, x2, y2, hauteur_saut, longueur_saut, debut, n_image, photo_mort
    global n_image_b, compt_rafraich_image, rafraich_image, corr_x, corr_y, photos, xf, photo_fond, photo_f1, photo_f2, photo_saute1, photo_saute2, photo_saute3
    global can_jeu, photo_f1, carre1, man, photo_man, texte, t_cheat, fenetre_jeu, alt_pose, photo_pose1, photo_pose2, touche, texte_pause, t_central, texte_collision
    global activ_bonus, cote_bonus, coord_bonus_x, coord_bonus_y, type_bonus, ico_bonus, chaine, cheat_bonus, var_bonus, longueur_run, mod_bonus

    # ***** VARIABLES ***** #

    go=False
    action_baisser = False
    action_sauter = False
    cheat = False
    affich_hitbox = False

    largeur_fenetre = 500
    hauteur_fenetre = 150
    score = 0

    largeur_obstacle = 20
    hauteur_obstacle = 20
    dx_obstacle, dy_obstacle = 3, 0
    vitesse = 10
    x1,y1 = -largeur_obstacle, 0

    hauteur_man = 40
    largeur_man = 20
    x2_o, y2_o = 20, hauteur_fenetre - hauteur_man
    x2, y2 = x2_o, y2_o

    hauteur_saut = hauteur_obstacle + 3
    longueur_saut = largeur_obstacle + 25
    debut = 0

    n_image = 5
    n_image_b = 6
    compt_rafraich_image = 0
    rafraich_image = 15
    corr_x, corr_y = 11, 15
    photos = []

    alt_pose = True

    touche = False

    texte_pause = 'Press p to start !'

    texte_collision = 'GAME OVER'

    cote_bonus = 30
    coord_bonus_x, coord_bonus_y = largeur_fenetre+cote_bonus,0
    activ_bonus = False
    type_bonus = 0
    cheat_bonus = False
    var_bonus = 0
    longueur_run = 10000
    mod_bonus = False

    # ***** PROGRAMME PRINCIPAL ***** #
    if first:
        fenetre_jeu = Toplevel()
        fenetre_jeu.title("Free Runner")
        fenetre_jeu.resizable(width=False, height=False)

    #Photos

    photo_fond = PhotoImage(file='immeubles.gif')
    xf = photo_fond.width()

    for i in range(1,7):
        photos.append(PhotoImage(file='court_'+str(i)+'.gif'))

    for i in range(1,8):
        photos.append(PhotoImage(file='roule_'+str(i)+'.gif'))

    photo_saute1 = PhotoImage(file='saute_1.gif')
    photo_saute2 = PhotoImage(file='saute_2.gif')
    photo_saute3 = PhotoImage(file='saute_3.gif')

    photo_pose1 = PhotoImage(file='pose_1.gif')
    photo_pose2 = PhotoImage(file='pose_2.gif')

    photo_mort = PhotoImage(file='mort.gif')

    # Widgets
    can_jeu = Canvas(fenetre_jeu,bg="white",height=hauteur_fenetre,width=largeur_fenetre)
    can_jeu.grid(row=0,rowspan=20, columnspan=3, column=0)

    photo_f1 = can_jeu.create_image(xf,0,image=photo_fond,anchor="ne")
    photo_f2 = can_jeu.create_image(xf,0,image=photo_fond,anchor="nw")

    carre1 = can_jeu.create_rectangle(x1,y1,x1+largeur_obstacle,y1+hauteur_obstacle,fill="black")
    if affich_hitbox:
        man = can_jeu.create_rectangle(x2,y2,x2+largeur_man,y2+hauteur_man,outline="red")

    ico_bonus = can_jeu.create_oval(coord_bonus_x,coord_bonus_y,coord_bonus_x+cote_bonus,coord_bonus_y+cote_bonus,fill="orange")
    photo_man = can_jeu.create_image(x2+corr_x,y2+hauteur_man-corr_y,image=photos[n_image])
    texte = can_jeu.create_text(largeur_fenetre-5,5,text=str(score),anchor="ne",font=(('MS','Sans','Serif'),8,"bold"),fill="black")
    t_cheat = can_jeu.create_text(5,5,text='',anchor="nw")
    t_central = can_jeu.create_text(int(largeur_fenetre/2),int(hauteur_fenetre/2), text=texte_pause, font=("Impact",30,"bold"), anchor="s")
    t_sous_central = can_jeu.create_text(int(largeur_fenetre/2),int(hauteur_fenetre/2), text='', font=(('MS','Sans','Serif'),12,"bold"), anchor="n")
    can_jeu.focus_set()

    can_jeu.bind('<Key>',action_clavier)
    can_jeu.bind('<Button-1>',clic_souris)

    chaine = can_jeu.create_text(largeur_fenetre/2,5,text='',anchor="n")

    if first:
        photob_pause=PhotoImage(file="pause_button.gif")
        photob_start=PhotoImage(file="start_button.gif")
        photob_return=PhotoImage(file="return_button.gif")
        bou1 = Button(fenetre_jeu,text='Retour', image=photob_return , command=fenetre_jeu.destroy)
        bou1.grid(row=21,column=0)
        bou2 = Button(fenetre_jeu, text='Demarrer', image=photob_start , command=start)
        bou2.grid(row=21,column=1)
        bou3 = Button(fenetre_jeu, text='Pause', image=photob_pause , command=stop)
        bou3.grid(row=21,column=2)

    arret()

    fenetre_jeu.mainloop()
    fenetre_jeu.destroy()