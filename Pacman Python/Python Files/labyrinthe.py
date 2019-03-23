from grille import *
from jeu import *
from fantome import*

DEPART=30
DEPART_X=150

def init():
    tableau=[]
    liste=[]
    for i in range (1,len(GRILLE)):
        if GRILLE[i]=="\n":
            tableau.append(liste)
            liste=[]                    #la fonction cree une liste jusqu'a ce qu'elle lise un retour a la ligne
        else:
            liste.append(GRILLE[i])       #Puis ajoute la liste créé a notre tableau
    return tableau        #La fonction renvoit le tableau


def est_mur(labyrinthe,lin,col):
    if labyrinthe[lin][col]==MUR: #On vérifie si le caractere a la position donnée est égale a la variable Mur (symbole "#")
        return True
    return False
        

def est_gomme(labyrinthe,lin,col):
    if labyrinthe[lin][col]==GOMME:  #On vérifie si le caractere a la position donnée est égale a la variable GOMME (symbole ".")
        return True
    return False

def dessine_mur(surface,lin,col):
    pygame.draw.rect(surface,BLEU,[T_CASE*col+DEPART_X,T_CASE*lin+DEPART,T_CASE,T_CASE],0)   #On déssine un mur a la bonne position

def dessine_gomme(surface,lin,col):
    pygame.draw.ellipse(surface,ORANGE,[T_CASE*col+DEPART_X+T_CASE/3,T_CASE*lin+DEPART+T_CASE/3,T_CASE/2.5,T_CASE/2.5],0) #On dessine un fruit
    
def dessine(labyrinthe,screen,pacman,fantomes):
    screen.fill(NOIR)
    for i in range (0,len(labyrinthe)):
        for j in range (0,len(labyrinthe[i])):  #Pour chaque ligne et chaque colonne :
            if est_mur(labyrinthe,i,j):
                dessine_mur(screen,i,j)            #La fonction vérifie si on a un mur ou un fruit, et dessine en utilisant la fonction correspondante
            if est_gomme(labyrinthe,i,j):
                dessine_gomme(screen,i,j)
            pygame.draw.circle(screen,JAUNE,[T_CASE*pacman["pos_c"]+DEPART_X+15,T_CASE*pacman["pos_l"]+DEPART+15],13,0)
            pygame.draw.rect(screen,ROUGE,[T_CASE*fantomes["rougey"]+DEPART_X,T_CASE*fantomes["rougex"]+DEPART,T_CASE,T_CASE],0)
            pygame.draw.rect(screen,ORANGE,[T_CASE*fantomes["orangey"]+DEPART_X,T_CASE*fantomes["orangex"]+DEPART,T_CASE,T_CASE],0)
            pygame.draw.rect(screen,CYAN,[T_CASE*fantomes["cyany"]+DEPART_X,T_CASE*fantomes["cyanx"]+DEPART,T_CASE,T_CASE],0)
            pygame.draw.rect(screen,ROSE,[T_CASE*fantomes["rosey"]+DEPART_X,T_CASE*fantomes["rosex"]+DEPART,T_CASE,T_CASE],0)   
    
def mange_gomme(labyrinthe,lin,col):
    labyrinthe[lin][col]=" "
    
def gagne(labyrinthe):
    for i in range (len(labyrinthe)):
        for j in range (len(labyrinthe[i])):
            if labyrinthe[i][j]==GOMME:
                return True
    return False
        
        

