import joueur


class plateau():
    largeur:int
    longueur:int
    pos_j1:int
    pos_j2:int
    block = []
    scene = None
    fps = 60
    def __init__(self,x,y):
        self.largeur=x
        self.longueur=y

    #Taille d'un fichier
    def len_of_file(self,file):
        cpt=0
        with open(file,'r') as f:
            while(True):
                c=f.read(1)
                if not c :
                    return cpt
                else:
                    cpt+=1 

    # Lit un fichier ffscene 
    def read_scene(self,file):
        cpt=0
        coeff = self.longueur//self.len_of_file(file)
        with open(file,'r') as f:
            while True:
                c = f.read(1)
                if not c:
                    if(cpt<self.longueur):
                        pass
                    break
                if(c=="1"):
                    if(cpt<self.longueur):
                        self.pos_j1=cpt*coeff
                elif c=="2":
                    if(cpt<self.longueur):
                        self.pos_j2=cpt*coeff
                elif c=="x":
                    if(cpt<self.longueur):
                        self.block.append(cpt*coeff)
                cpt+=1
                    
    #reset position des joueurs
    def reset_pos(self,j1:joueur,j2:joueur):
        j1.x=self.pos_j1
        j2.x=self.pos_j2
                
    def end_game(self,j1:joueur,j2:joueur):
        if(j1.score==3 or j2.score==3):
            return True
        return False

    #Reset le jeu à la fin d'une partie
    def reset_jeu(self,j1:joueur,j2:joueur):
        self.reset_pos(j1,j2)
        j1.score=0
        j2.score=0
        self.scene=None
