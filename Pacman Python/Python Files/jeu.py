import pygame
from grille import *
import pacman
from __main__ import *
from couleur import *
import labyrinthe
import fantome
message=True
fin=False
def boucle(parametre):
    win=pygame.image.load("win.png")
    lose=pygame.image.load("lose.png")
    fin=False
    message=True
    laby=labyrinthe.init()
    while parametre["play"] == True:  #Tant qu'on arrete pas le jeu
        parametre["clock"].tick(10)
        traite_event(parametre,laby)
        if parametre["pacman"]["vivant"]:
            if labyrinthe.gagne(laby):
                labyrinthe.dessine(laby,parametre["surface"],parametre["pacman"],parametre["fantomes"]) #On traite les evenements et on affiche le labyrinthe
                mise_a_jour(parametre,laby)
            if labyrinthe.gagne(laby)==False and message==True:
                message=False
                print("Vous avez Gagné ! Voulez-vous Rejouer ? ( Appuyez sur O pour Oui et N pour Non )")
                parametre["surface"].fill(NOIR)
                parametre["surface"].blit(win,(300,130))
        else:
            if message==True:
                message=False
                print("Vous avez perdu ! Voulez-vous Rejouer ? ( Appuyez sur O pour Oui et N pour Non )")
                parametre["surface"].fill(NOIR)
                parametre["surface"].blit(lose,(300,130))
                
            
        pygame.display.flip()
    
def init():
    SIZE=[1080,720]
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Pacman Python")             #On définit tous les parametres
    screen = pygame.display.set_mode(SIZE)
    parametres={"size" : SIZE,"clock" : clock,"surface" : screen,"play" : True} #Qu'on stock dans un dictionnaire
    parametres["pacman"]=pacman.init(POS_PACMAN[0],POS_PACMAN[1],pacman.STOP)
    parametres["fantomes"]=fantome.fantinit()
    return parametres     #On renvoit ce dictionnaire

def quitte():
    pygame.quit()
def mise_a_jour(parametre,labyrinthe):
    pacman.met_a_jour(parametre,labyrinthe)
    fantome.perte(parametre)
    pygame.display.flip()

def traite_event(parametre,laby):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:             #Si l'utilisateur appuie sur la croix
            parametre["play"]=False
            parametre["rejouer"]=False
        elif event.type==pygame.KEYDOWN:              #Ou s'il appuie sur ECHAP:
            if event.key==pygame.K_ESCAPE:
                parametre["rejouer"]=False
                parametre["play"]=False            #On arrete le jeu
            if labyrinthe.gagne(laby):
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    if laby[parametre["pacman"]["pos_l"]][parametre["pacman"]["pos_c"]-1]!=MUR:
                        pacman.depl_gauche(parametre["pacman"])
                    else:
                        parametre["pacman"]["attente"]=pacman.GAUCHE
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    if laby[parametre["pacman"]["pos_l"]][parametre["pacman"]["pos_c"]+1]!=MUR:
                        pacman.depl_droite(parametre["pacman"])
                    else:
                        parametre["pacman"]["attente"]=pacman.DROITE
                if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    if laby[parametre["pacman"]["pos_l"]+1][parametre["pacman"]["pos_c"]]!=MUR:
                        pacman.depl_bas(parametre["pacman"])
                    else:
                        parametre["pacman"]["attente"]=pacman.BAS
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    if laby[parametre["pacman"]["pos_l"]-1][parametre["pacman"]["pos_c"]]!=MUR:
                        pacman.depl_haut(parametre["pacman"])
                    else:
                        parametre["pacman"]["attente"]=pacman.HAUT
            if labyrinthe.gagne(laby)==False or parametre["pacman"]["vivant"]==False:
                if event.key==pygame.K_o:
                    parametre["rejouer"]=True
                    parametre["play"]=False
                elif event.key==pygame.K_n:
                    parametre["rejouer"]=False
                    parametre["play"]=False
            
    
        
