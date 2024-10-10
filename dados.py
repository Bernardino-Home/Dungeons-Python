from model import Heroi, Monstro

class HeroiRepository:                
    def __init__(self):
        self.herois = []

    def cadastrar_heroi(self, heroi):                          #recebe objeto da classe heroi
        heroi_existente = self.get_heroi_nome(heroi.nome)      #verifica se ja existe heroi

        if heroi_existente is None:                            #adiciona À lista
            self.herois.append(heroi)
            print(f"Herói {heroi.nome} criado! Vamos a isto!")
        else:
            print(f"Herói {heroi.nome} já está na fila!")

    def get_heroi_nome(self, nome):                           #varre a lista e devolve o heroi
        for heroi in self.herois:
            if heroi.nome == nome:
                return heroi
        return None
    
class MonstroRepository:
    def __init__(self):
        self.monstro = []

    def get_monstro_nome(self, nome): # ter isto ou nao ter é a mm coisa....
        for monstro in self.monstro:
            if monstro.nome == nome:
                return monstro
        return None
    
    def cadastrar_Monstro(self, monstro):      # adiciona monstro à lista
        self.monstro.append(monstro)
        print(f"Monstro {monstro} foi encontrado!")