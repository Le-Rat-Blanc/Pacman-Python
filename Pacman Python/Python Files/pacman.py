from grille import *
import fantome
from labyrinthe import *
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3
STOP=4
ATTENTEHAUT=5
ATTENTEBAS=6
ATTENTEGAUCHE=7
ATTENTEDROITE=8

def init(y,x,di):
    pacman={"vivant":True, "pos_l":y,"pos_c":x,"direc":di,"depl_l":0,"depl_c":0,"attente":4}
    return pacman

def depl_haut(pacman):
    pacman["depl_l"]=-1
    pacman["direc"]=HAUT

def depl_bas(pacman):
    pacman["depl_l"]=1
    pacman["depl_c"]=0
    pacman["direc"]=BAS

def depl_gauche(pacman):
    pacman["depl_c"]=-1
    pacman["depl_l"]=0    
    pacman["direc"]=GAUCHE

def depl_droite(pacman):
    pacman["depl_c"]=1
    pacman["depl_l"]=0
    pacman["direc"]=DROITE

def met_a_jour(parametre,labyrinthe):
    if parametre["pacman"]["vivant"]:
            if labyrinthe[parametre["pacman"]["pos_l"]-1][parametre["pacman"]["pos_c"]]!=MUR and parametre["pacman"]["attente"]==HAUT:
                parametre["pacman"]["direc"]=HAUT
                parametre["pacman"]["attente"]=STOP
            elif labyrinthe[parametre["pacman"]["pos_l"]+1][parametre["pacman"]["pos_c"]]!=MUR and parametre["pacman"]["attente"]==BAS:
                parametre["pacman"]["direc"]=BAS
                parametre["pacman"]["attente"]=STOP
            elif labyrinthe[parametre["pacman"]["pos_l"]][parametre["pacman"]["pos_c"]+1]!=MUR and parametre["pacman"]["attente"]==DROITE:
                parametre["pacman"]["direc"]=DROITE
                parametre["pacman"]["attente"]=STOP
            elif labyrinthe[parametre["pacman"]["pos_l"]][parametre["pacman"]["pos_c"]-1]!=MUR and parametre["pacman"]["attente"]==GAUCHE:
                parametre["pacman"]["direc"]=GAUCHE
                parametre["pacman"]["attente"]=STOP
                

            if parametre["pacman"]["direc"]==HAUT:
                if labyrinthe[parametre["pacman"]["pos_l"]-1][parametre["pacman"]["pos_c"]]!=MUR:
                    parametre["pacman"]["pos_l"]-=1
                    fantome.deplacements(parametre["fantomes"],labyrinthe)
            elif parametre["pacman"]["direc"]==BAS:
                if labyrinthe[parametre["pacman"]["pos_l"]+1][parametre["pacman"]["pos_c"]]!=MUR:
                    parametre["pacman"]["pos_l"]+=1
                    fantome.deplacements(parametre["fantomes"],labyrinthe)

            elif parametre["pacman"]["direc"]==DROITE:
                if labyrinthe[parametre["pacman"]["pos_l"]][parametre["pacman"]["pos_c"]+1]!=MUR:
                    parametre["pacman"]["pos_c"]+=1
                    fantome.deplacements(parametre["fantomes"],labyrinthe)
                    
            elif parametre["pacman"]["direc"]==GAUCHE:
                if labyrinthe[parametre["pacman"]["pos_l"]][parametre["pacman"]["pos_c"]-1]!=MUR:
                    parametre["pacman"]["pos_c"]-=1
                    fantome.deplacements(parametre["fantomes"],labyrinthe)
            mange_gomme(labyrinthe,parametre["pacman"]["pos_l"],parametre["pacman"]["pos_c"])
            
