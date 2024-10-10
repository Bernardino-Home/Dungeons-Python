class Heroi:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

class Guerreiro(Heroi):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome,vida,ataque)

class Mago(Heroi):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome,vida,ataque)        

class Monstro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

class Ogro(Monstro):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome,vida,ataque)    

class Dragao(Monstro):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome,vida,ataque) 

class Caerbannog(Monstro):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome,vida,ataque) 