
from joueur import joueur
import curses
import plateau
import pygame
import time

#ajout block affichage
def add_block(arg,i,j):
    arg.addstr(i,j,"x")

#Savoir si il y a un block
def can_pass(pos_j1,block):
    for i in range(len(block)):
        if(pos_j1==block[i]):  
            return False
    return True

#Savoir si le joueur est au dessus d'un bloc
def no_block_under(pos_x,block):
    for i in range(len(block)):
        if(pos_x==block[i]):  
            return False
    return True

#Affiche menu
def draw_menu(arg,plateau):
    current_pos = 1
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    afficher = True

    while(afficher):
        key = arg.getch()

        if(key==curses.KEY_DOWN and current_pos<3):
            current_pos+=1
        if(key==curses.KEY_UP and current_pos>1):
            current_pos-=1
        if(key==curses.KEY_ENTER or key == 10):
            if(current_pos==1):
                arg.clear()
                current_pos_2=1
                if(plateau.scene==None):
                    while(1):
                        key=arg.getch()

                        if(key==curses.KEY_DOWN and current_pos_2<3):
                            current_pos_2+=1
                        if(key==curses.KEY_UP and current_pos_2>1):
                            current_pos_2-=1

                        if(current_pos_2==1):
                            arg.addstr(plateau.largeur//2-3,plateau.longueur//2,"Choisir Scène :")
                            arg.attron(curses.color_pair(1))
                            arg.addstr(plateau.largeur//2-2,plateau.longueur//2,"Scène 1")
                            arg.attroff(curses.color_pair(1))
                            arg.addstr(plateau.largeur//2-1,plateau.longueur//2,"Scène 2")
                            arg.addstr(plateau.largeur//2,plateau.longueur//2,"Scène 3")
                        if(current_pos_2==2):
                            arg.addstr(plateau.largeur//2-3,plateau.longueur//2,"Choisir Scène :")
                            arg.addstr(plateau.largeur//2-2,plateau.longueur//2,"Scène 1")
                            arg.attron(curses.color_pair(1))
                            arg.addstr(plateau.largeur//2-1,plateau.longueur//2,"Scène 2")
                            arg.attroff(curses.color_pair(1))
                            arg.addstr(plateau.largeur//2,plateau.longueur//2,"Scène 3")
                        if(current_pos_2==3):
                            arg.addstr(plateau.largeur//2-3,plateau.longueur//2,"Choisir Scène :")
                            arg.addstr(plateau.largeur//2-2,plateau.longueur//2,"Scène 1")
                            arg.addstr(plateau.largeur//2-1,plateau.longueur//2,"Scène 2")
                            arg.attron(curses.color_pair(1))
                            arg.addstr(plateau.largeur//2,plateau.longueur//2,"Scène 3")
                            arg.attroff(curses.color_pair(1))
                        
                        if(key==curses.KEY_ENTER or key == 10):
                            if(current_pos_2==1):
                                plateau.scene="scenes/scene1.ffscene"
                                afficher=False
                                break
                            if(current_pos_2==2):
                                plateau.scene="scenes/scene2.ffscene"
                                afficher=False
                                break
                            if(current_pos_2==3):
                                plateau.scene="scenes/scene3.ffscene"
                                afficher=False
                                break
                break
            if(current_pos==2):
                arg.clear()
                while(1):
                    key=arg.getch()
                    arg.addstr(plateau.largeur//2-3,plateau.longueur//2-20, "Joueur 1 :")
                    arg.addstr(plateau.largeur//2-2,plateau.longueur//2-20, "d => aller à droite")
                    arg.addstr(plateau.largeur//2-1,plateau.longueur//2-20, "q => aller à gauche")
                    arg.addstr(plateau.largeur//2,plateau.longueur//2-20, "z => attaquer")
                    arg.addstr(plateau.largeur//2+1,plateau.longueur//2-20, "s => bloquer")
                    arg.addstr(plateau.largeur//2+2,plateau.longueur//2-20, "a => saut à gauche")
                    arg.addstr(plateau.largeur//2+3,plateau.longueur//2-20, "e => saut à droite")

                    arg.addstr(plateau.largeur//2-3,plateau.longueur//2+5, "Joueur 2 :")
                    arg.addstr(plateau.largeur//2-2,plateau.longueur//2+5, "-> => aller à droite")
                    arg.addstr(plateau.largeur//2-1,plateau.longueur//2+5, "<- => aller à gauche")
                    arg.addstr(plateau.largeur//2,plateau.longueur//2+5, "o => attaquer")
                    arg.addstr(plateau.largeur//2+1,plateau.longueur//2+5, "p => bloquer")
                    arg.addstr(plateau.largeur//2+2,plateau.longueur//2+5, "l => saut à gauche")
                    arg.addstr(plateau.largeur//2+3,plateau.longueur//2+5, "m => saut à droite")

                    arg.addstr(plateau.largeur//2+6,plateau.longueur//2-10, "Appuyer sur q pour revenir en arrère")



                    if(key==ord('q')):
                        arg.clear()
                            
                        break
            elif current_pos==3:
                return False

        if(current_pos==1):
            arg.attron(curses.color_pair(1))
            arg.addstr(plateau.largeur//2-2,plateau.longueur//2, "Jouer")
            arg.attroff(curses.color_pair(1))
            arg.addstr(plateau.largeur//2-1,plateau.longueur//2, "Les Commandes")
            arg.addstr(plateau.largeur//2,plateau.longueur//2, "Quitter")
        if(current_pos==2):
            arg.addstr(plateau.largeur//2-2,plateau.longueur//2, "Jouer")
            arg.attron(curses.color_pair(1))
            arg.addstr(plateau.largeur//2-1,plateau.longueur//2, "Les Commandes")
            arg.attroff(curses.color_pair(1))
            arg.addstr(plateau.largeur//2,plateau.longueur//2, "Quitter")
        if(current_pos==3):
            arg.addstr(plateau.largeur//2-2,plateau.longueur//2, "Jouer")
            arg.addstr(plateau.largeur//2-1,plateau.longueur//2, "Les Commandes")
            arg.attron(curses.color_pair(1))
            arg.addstr(plateau.largeur//2,plateau.longueur//2, "Quitter")
            arg.attroff(curses.color_pair(1))

#Affiche 'plateau' du jeu
def draw_plateau(arg,joueur_1,joueur_2,p):
    ##print score
    arg.addstr(p.largeur//2-3,p.longueur//2-3,"J_1 :"+str(joueur_1.score))
    arg.addstr(p.largeur//2-2,p.longueur//2-3,"J_2 :"+str(joueur_2.score))
    ##print bloc sur terrain
    for i in range(len(p.block)):
       add_block(arg,p.largeur-4,p.block[i])
    ##print bordure block
    for i in range(p.largeur-3):
        add_block(arg,i,3)
        add_block(arg,i,p.longueur-3)
    ##print sol
    for i in range(3,p.longueur-3):
        arg.addstr(p.largeur-3,i,"#")

#efface ancienne position du joueur
def eff_prev_pos(arg,j:joueur):
    if(j.i==1):
        #joueur1
        arg.addstr(j.y-3,j.x," ")

        arg.addstr(j.y-2,j.x," ")
        arg.addstr(j.y-2,j.x+1," ")
        if(j.statut=="attack"):
            arg.addstr(j.y-2,j.x+2," ")
        elif j.statut=="block":
            arg.addstr(j.y-2,j.x+2," ")
        else:  
            arg.addstr(j.y-2,j.x+2," ")

        arg.addstr(j.y-1,j.x," ")
        arg.addstr(j.y,j.x," ")
        arg.addstr(j.y,j.x-1," ")
    else:
        #joueur2
        arg.addstr(j.y-3,j.x," ")

        arg.addstr(j.y-2,j.x," ")
        arg.addstr(j.y-2,j.x-1," ")
        arg.addstr(j.y-2,j.x-2," ")
        if(j.statut=="attack"):
            arg.addstr(j.y-2,j.x-2," ")
        elif j.statut=="block":
            arg.addstr(j.y-2,j.x-2," ")
        else:  
            arg.addstr(j.y-2,j.x-2," ")
            
        arg.addstr(j.y-1,j.x," ")
        arg.addstr(j.y,j.x," ")
        arg.addstr(j.y,j.x+1," ")

#Affichage joueur
def draw_joueur(arg,j1:joueur,j2:joueur,plateau):

    draw_plateau(arg,j1,j2,plateau)
    #joueur1
    arg.addstr(j1.y-3,j1.x,"O")

    arg.addstr(j1.y-2,j1.x,"|")
    arg.addstr(j1.y-2,j1.x+1,"_")
    if(j1.statut=="attack"):
        arg.addstr(j1.y-2,j1.x+2,"_")
    elif j1.statut=="block":
        arg.addstr(j1.y-2,j1.x+2,"|")
    else:  
        arg.addstr(j1.y-2,j1.x+2,"/")

    arg.addstr(j1.y-1,j1.x,"|")
    arg.addstr(j1.y,j1.x,"|")
    arg.addstr(j1.y,j1.x-1,"/")

    #joueur2
    arg.addstr(j2.y-3,j2.x,"O")

    arg.addstr(j2.y-2,j2.x,"|")
    arg.addstr(j2.y-2,j2.x-1,"_")
    arg.addstr(j2.y-2,j2.x-2,"\\")
    if(j2.statut=="attack"):
        arg.addstr(j2.y-2,j2.x-2,"_")
    elif j2.statut=="block":
        arg.addstr(j2.y-2,j2.x-2,"|")
    else:  
        arg.addstr(j2.y-2,j2.x-2,"\\")
        
    arg.addstr(j2.y-1,j2.x,"|")
    arg.addstr(j2.y,j2.x,"|")
    arg.addstr(j2.y,j2.x+1,"\\")


def main(arg):
    clock = pygame.time.Clock()
    
    #enleve curseur
    curses.curs_set(0)
    arg.nodelay(1)

    largeur, longueur = arg.getmaxyx()

    p = plateau.plateau(largeur,longueur)

    if(draw_menu(arg,p)==False):
        jeu=False

    #lire la scène choisis
    p.read_scene(p.scene)

    joueur_1 = joueur(1,p.pos_j1)
    joueur_2 = joueur(2,p.pos_j2)

    j1_over_block = False
    j2_over_block = False

    joueur_1.y= p.largeur-4
    joueur_2.y= p.largeur-4

    attaque_j1=joueur_1.v_attack
    attaque_j2=joueur_2.v_attack

    block_j1=joueur_1.dur_block
    block_j2=joueur_2.dur_block

    jeu = True

    arg.clear()

    while jeu:
        clock.tick(p.fps)

        key = arg.getch()             

        attaque_j1+=1
        attaque_j2+=1
        
        block_j1+=1
        block_j2+=1

        # Appuyer sur 'echap' => met le jeu en pause
        if(key==27):
            arg.clear()
            if(draw_menu(arg,p)==False):
                jeu=False
            arg.clear()

        ###joueur2
        #droite
        if(key==curses.KEY_RIGHT and can_pass(joueur_2.x+1,p.block) and joueur_2.x+1<p.longueur-3):
            eff_prev_pos(arg,joueur_2)
            if(j2_over_block):
                joueur_2.y+=1 
                j2_over_block=False 
            joueur_2.x+=1
 
        if(key==curses.KEY_LEFT and  can_pass(joueur_2.x-1,p.block)and joueur_2.x-2>joueur_1.x):
            eff_prev_pos(arg,joueur_2)
            if(j2_over_block):
                joueur_2.y+=1 
                j2_over_block=False
            joueur_2.x-=1
               
        
        #attack
        if(key==ord('o')): 
            joueur_2.statut="attack"
            eff_prev_pos(arg,joueur_2)
            attaque_j2=0
        
        #attacking range
        if(attaque_j2==joueur_2.v_attack and joueur_2.toucher(joueur_1)):
            if(attaque_j2!=attaque_j1):
                joueur_2.score+=1
            eff_prev_pos(arg,joueur_1)
            eff_prev_pos(arg,joueur_2)
            p.reset_pos(joueur_1,joueur_2)
                 
        
        #block
        if(key==ord('p')): 
            joueur_2.statut="block"
            eff_prev_pos(arg,joueur_2)
        
            block_j2=0
        
        #saut gauche
        if(key==ord('l')): 
            if(not j2_over_block):
                eff_prev_pos(arg,joueur_2)
                joueur_2.y-=1
                draw_joueur(arg,joueur_1,joueur_2,p)
                arg.refresh()
                time.sleep(0.03)
                if(joueur_2.x-2>joueur_1.x):
                    eff_prev_pos(arg,joueur_2)
                    joueur_2.x-=1
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()
                    time.sleep(0.03)
                if(no_block_under(joueur_2.x,p.block)):
                    eff_prev_pos(arg,joueur_2)
                    joueur_2.y+=1
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()
                    time.sleep(0.03)
                else:
                    j2_over_block=True

        #saut droite
        if(key==ord('m')):
            if(not j2_over_block):
                eff_prev_pos(arg,joueur_2) 
                joueur_2.y-=1            
                draw_joueur(arg,joueur_1,joueur_2,p)
                arg.refresh()
                time.sleep(0.03)

                if(joueur_2.x+1<p.longueur-3):
                    eff_prev_pos(arg,joueur_2)
                    joueur_2.x+=1            
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()
                    time.sleep(0.03)

                if(no_block_under(joueur_2.x,p.block)):
                    eff_prev_pos(arg,joueur_2)
                    joueur_2.y+=1            
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh() 
                    time.sleep(0.03)
                else:
                    j2_over_block=True

        ###joueur1
        #droite
        if(key==ord('d') and can_pass(joueur_1.x+1,p.block) and joueur_1.x+2<joueur_2.x): 
            eff_prev_pos(arg,joueur_1)
            if(j1_over_block):
                joueur_1.y+=1 
                j1_over_block=False
            joueur_1.x+=1
               
        
        #gauche
        if(key==ord('q') and can_pass(joueur_1.x-1,p.block) and joueur_1.x-1>3): 
            eff_prev_pos(arg,joueur_1)
            if(j1_over_block):
                joueur_1.y+=1 
                j1_over_block=False
            joueur_1.x-=1
             
        
        #attack
        if(key==ord('z')): 
            joueur_1.statut="attack"
            eff_prev_pos(arg,joueur_1)            
            attaque_j1=0
        
        if(attaque_j1==joueur_1.v_attack and joueur_1.toucher(joueur_2)):
            if(attaque_j1!=attaque_j2):
                joueur_1.score+=1
            eff_prev_pos(arg,joueur_1)
            eff_prev_pos(arg,joueur_2)
            p.reset_pos(joueur_1,joueur_2)
                 
        #block
        if(key==ord('s')): 
            joueur_1.statut="block"
            eff_prev_pos(arg,joueur_1)        
            block_j1=0
 
        #saut gauche
        if(key==ord('a')):
            if(not j1_over_block):
                eff_prev_pos(arg,joueur_1)
                joueur_1.y-=1
                draw_joueur(arg,joueur_1,joueur_2,p)
                arg.refresh()
                time.sleep(0.03)
                if(joueur_1.x-1>3):
                    eff_prev_pos(arg,joueur_1)
                    joueur_1.x-=1
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()
                    time.sleep(0.03)

                if(no_block_under(joueur_1.x,p.block)):
                    eff_prev_pos(arg,joueur_1)
                    joueur_1.y+=1
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()
                    time.sleep(0.03)
                else:
                    j1_over_block=True
        
        #saut droite
        if(key==ord('e')):
            if(not j1_over_block):
                eff_prev_pos(arg,joueur_1) 
                joueur_1.y-=1
                draw_joueur(arg,joueur_1,joueur_2,p)
                arg.refresh()
                time.sleep(0.03)
                
                if(joueur_1.x+2<joueur_2.x):
                    eff_prev_pos(arg,joueur_1)
                    joueur_1.x+=1
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()                    
                    time.sleep(0.03)

                if(no_block_under(joueur_1.x,p.block)):
                    eff_prev_pos(arg,joueur_1)
                    joueur_1.y+=1
                    draw_joueur(arg,joueur_1,joueur_2,p)
                    arg.refresh()   
                    time.sleep(0.03)
                else:
                    j1_over_block=True

        #Retour position rest
        if(attaque_j2>joueur_2.v_attack and block_j2>joueur_2.dur_block):
            joueur_2.statut="rest"
        if(attaque_j1>joueur_1.v_attack and block_j1>joueur_2.dur_block):
            joueur_1.statut="rest"

        # Fin Du jeu ?
        if(p.end_game(joueur_1,joueur_2)):
            if(joueur_1.score>joueur_2.score):
                arg.addstr(p.largeur//2,p.longueur//2-5,"Le gagnant est Joueur 1")
            else:
                arg.addstr(p.largeur//2,p.longueur//2-5,"Le gagnant est Joueur 2")
            draw_joueur(arg,joueur_1,joueur_2,p)
            arg.refresh()
            time.sleep(5)
            arg.clear()
            p.reset_jeu(joueur_1,joueur_2)
            if(draw_menu(arg,p)==False):
                jeu=False
            else:
                p.block=[]
                #Choisis la scène que tu veux
                p.read_scene(p.scene)
                joueur_1 = joueur(1,p.pos_j1)
                joueur_2 = joueur(2,p.pos_j2)
                joueur_1.y= p.largeur-4
                joueur_2.y= p.largeur-4
                j1_over_block = False
                j2_over_block = False

            arg.clear()
        
        draw_joueur(arg,joueur_1,joueur_2,p)
        arg.refresh()

curses.wrapper(main)
