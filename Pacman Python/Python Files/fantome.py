from random import randint
from grille import *
def fantinit():
    fantomes={"rougex":9,"rougey":12,"orangex":10,"orangey":11,"cyanx":10,"cyany":12,"rosex":10,"rosey":13}
    return fantomes
def deplacements(fantomes,laby):
        possibility = False
        while not possibility:
            pos=randint(0,4)
            if pos==0:
                if laby[fantomes["rougex"]-1][fantomes["rougey"]]!=MUR:
                    possibility=True
                    fantomes["rougex"]-=1
            elif pos==1:
                if laby[fantomes["rougex"]][fantomes["rougey"]+1]!=MUR:
                    possibility=True
                    fantomes["rougey"]+=1
            elif pos==2:
                if laby[fantomes["rougex"]+1][fantomes["rougey"]]!=MUR:
                    possibility=True
                    fantomes["rougex"]+=1
            elif pos==4:
                if laby[fantomes["rougex"]][fantomes["rougey"]-1]!=MUR:
                    possibility=True
                    fantomes["rougey"]-=1
        possibility = False
        while not possibility:
            pos=randint(0,4)
            if pos==0:
                if laby[fantomes["orangex"]-1][fantomes["orangey"]]!=MUR:
                    possibility=True
                    fantomes["orangex"]-=1
            elif pos==1:
                if laby[fantomes["orangex"]][fantomes["orangey"]+1]!=MUR:
                    possibility=True
                    fantomes["orangey"]+=1
            elif pos==2:
                if laby[fantomes["orangex"]+1][fantomes["orangey"]]!=MUR:
                    possibility=True
                    fantomes["orangex"]+=1
            elif pos==4:
                if laby[fantomes["orangex"]][fantomes["orangey"]-1]!=MUR:
                    possibility=True
                    fantomes["orangey"]-=1
        possibility = False
        while not possibility:
            pos=randint(0,4)
            if pos==0:
                if laby[fantomes["cyanx"]-1][fantomes["cyany"]]!=MUR:
                    possibility=True
                    fantomes["cyanx"]-=1
            elif pos==1:
                if laby[fantomes["cyanx"]][fantomes["cyany"]+1]!=MUR:
                    possibility=True
                    fantomes["cyany"]+=1
            elif pos==2:
                if laby[fantomes["cyanx"]+1][fantomes["cyany"]]!=MUR:
                    possibility=True
                    fantomes["cyanx"]+=1
            elif pos==4:
                if laby[fantomes["cyanx"]][fantomes["cyany"]-1]!=MUR:
                    possibility=True
                    fantomes["cyany"]-=1
        possibility = False
        while not possibility:
            pos=randint(0,4)
            if pos==0:
                if laby[fantomes["rosex"]-1][fantomes["rosey"]]!=MUR:
                    possibility=True
                    fantomes["rosex"]-=1
            elif pos==1:
                if laby[fantomes["rosex"]][fantomes["rosey"]+1]!=MUR:
                    possibility=True
                    fantomes["rosey"]+=1
            elif pos==2:
                if laby[fantomes["rosex"]+1][fantomes["rosey"]]!=MUR:
                    possibility=True
                    fantomes["rosex"]+=1
            elif pos==4:
                if laby[fantomes["rosex"]][fantomes["rosey"]-1]!=MUR:
                    possibility=True
                    fantomes["rosey"]-=1
        
    
def perte(parametre):
    if parametre["pacman"]["pos_c"] <= parametre["fantomes"]["rougey"]+1 and parametre["pacman"]["pos_c"] >= parametre["fantomes"]["rougey"]-1 and parametre["pacman"]["pos_l"] <= parametre["fantomes"]["rougex"]+1 and parametre["pacman"]["pos_l"] >= parametre["fantomes"]["rougex"]-1:
        parametre["pacman"]["vivant"]=False
    if parametre["pacman"]["pos_c"] <= parametre["fantomes"]["rosey"]+1 and parametre["pacman"]["pos_c"] >= parametre["fantomes"]["rosey"]-1 and parametre["pacman"]["pos_l"] <= parametre["fantomes"]["rosex"]+1 and parametre["pacman"]["pos_l"] >= parametre["fantomes"]["rosex"]-1:
        parametre["pacman"]["vivant"]=False
    if parametre["pacman"]["pos_c"] <= parametre["fantomes"]["cyany"]+1 and parametre["pacman"]["pos_c"] >= parametre["fantomes"]["cyany"]-1 and parametre["pacman"]["pos_l"] <= parametre["fantomes"]["cyanx"]+1 and parametre["pacman"]["pos_l"] >= parametre["fantomes"]["cyanx"]-1:
        parametre["pacman"]["vivant"]=False
    if parametre["pacman"]["pos_c"] <= parametre["fantomes"]["orangey"]+1 and parametre["pacman"]["pos_c"] >= parametre["fantomes"]["orangey"]-1 and parametre["pacman"]["pos_l"] <= parametre["fantomes"]["orangex"]+1 and parametre["pacman"]["pos_l"] >= parametre["fantomes"]["orangex"]-1:
        parametre["pacman"]["vivant"]=False