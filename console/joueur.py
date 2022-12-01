
class joueur:
    #position
    x: int
    y: int
    #quel joueur 1 ou 2
    i:int
    #vitesse
    v_attack = 250
    dur_block = 500
    #score du joueur
    score = 0

    def __init__(self,j,x):
        self.i=j
        if j==1:
            self.x=x
        else:
            self.x=x
        self.y=4
        self.statut = "rest"
    

    def end_attack(self,t):
        if(self.v_attack>t):
            self.statut="rest"

    def toucher(self,j2):
        if(abs(j2.x-self.x)<4):
            if(self.statut=="attack" and j2.statut!="block"):
                return True
            else:
                return False
        return False

