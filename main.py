"""
Os alunos devem criar um RPG onde heróis enfrentam monstros em batalhas.
Cada tipo de herói tem suas próprias habilidades e cada monstro reage de maneira diferente aos ataques.

Conceitos:

Herança: Uma classe Personagem que serve de base para Heroi e Monstro.
Polimorfismo: Heróis e monstros têm habilidades e comportamentos diferentes ao atacar e defender.
Instruções:

Crie uma classe base Personagem com atributos: nome, vida e ataque.
Crie uma classe Heroi com subclasses: Guerreiro e Mago, onde cada um ataca de maneira diferente (por exemplo, Guerreiro usa espada, Mago usa magia).
Crie uma classe Monstro com subclasses: Ogro e Dragao, onde cada um tem uma resistência ou fraqueza diferente.
Crie um sistema de batalha onde o herói enfrenta o monstro até que um dos dois perca toda a vida.



classes
class Personagem -> nome, vida, ataque

class Heroi(Personagem) ->nome, vida, ataque
class Guerreiro(Heroi) -> ataca
class Mago(Heroi)->ataca

class Monstro(Personagem)-> nome, vida, ataque?
class Ogro(Monstro) -> defende?
class Dragao(Monstro)-> defende?

Ogre - 25% resistencia dano fisico
Ogre - 0% resistencia magia

Dragao - 75% resistencia magia
Dragao - 50% resistencia dano fisico

se dado random 0-20 = 20, entao dano = 3x?

tipos de ataque?
se espada entao mudar dano
se machado entao mudar dano
se lança entao mudar dano

se magia poison ogre - dano alto
se magia fogo ogre - dano alto
se magia poison dragao - dano normal
se magia fogo dragao - dano cócegas
se magia gelo dragao - dano 20% mais alto?

com as moedas/arcado tesouro, tirar um numero random
e com isso comprar arma
0-5 - dagger - dano reduzido em 20% | agua dano = ogro, menos 80% dragao
6-10 - espada - dano =              | veneno menos 60% ogro, 1.2dragao
11-15 - machado - dano x1.2         | fogo 1.2 ogro, 50% dragao
16-20 - lança - dano x1.4           | raio 1,8 ogro e dragao

"""

from dados import HeroiRepository, MonstroRepository
from model import Guerreiro, Mago, Ogro, Dragao, Caerbannog
import random

class Menu:
    def __init__(self):
        self.opcao = None
        self.heroi_repository = HeroiRepository()
        self.monstro_repository = MonstroRepository()
        self.heroi_escolhido = None
        self.menu = """
*** MENU ***
---Bem vindo a Dungeons and Python---
1 - História / Estória / Como tudo começou....
2 - Adicionar Heroi
3 - Adicionar Monstro
4 - Iniciar batalha
5 - Regras
0 - Quit D&P
"""
    def executar(self):
        while self.opcao != 0:
            print(self.menu)
            self.opcao = int(input("Selecione uma opção:\n"))

            if self.opcao == 1:
                self.historia_estoria()
            elif self.opcao == 2:
                self.adicionar_heroi()
            elif self.opcao == 3:
                self.adicionar_monstro()
            elif self.opcao == 4:
                self.iniciar_batalha()
            elif self.opcao == 5:
                self.regras_regras()
            elif self.opcao == 0:
                print("Não percas a próxima campanha porque nós também não!!")
                break
            else:
                print("Blue screen of death ")

    def historia_estoria(self):
        print(f"\nEra uma vez um heroi...")
        print(f"Que deambulava pelas selvas de Pythonlândia")
        print(f"Fugia de Marcovsky, the Teacher")
        print(f"Mas Marcovksy (Marcos para os alunos) sempre no seu encalço.")
        print(f"Fugia já há tanto tempo que lhe deu a fome....\n")


    
    def adicionar_heroi(self):
        nome = input("Qual o nome do nosso herói?")
        profissao = input("O herói é Guerreiro ou Mago?").lower()
        vida = int(input("Quanto Hp tem o nosso herói?"))
        ataque = int(input("Quanto ataque tem o nosso herói?"))

        if nome == "ni": #easter egg
            print(f"The  knight who says NI has been summoned!")
            vida*=1000
            ataque*=1000

        if profissao == "guerreiro":
            heroi = Guerreiro(nome, vida, ataque)

        elif profissao == "mago":
            heroi = Mago(nome, vida, ataque)
        else:
            print("Profissão inválida")
            return

        self.heroi_repository.cadastrar_heroi(heroi)
        self.heroi_escolhido = heroi
   
    def adicionar_monstro(self):

        if self.heroi_escolhido == None:
            print("Precisa de escolher um herói.")
            return

        nome_monstro = input("\nEscolhe com quem combater:\n Ogro ou Dragão?\n ou Caerbannog?\n").lower()

        if nome_monstro == 'ogro':
            vida_monstro = self.heroi_escolhido.vida*1.3 #ogre tem mais 30% vida que heroi
            ataque_monstro = self.heroi_escolhido.ataque*1.2 #ogre tem mais 20% ataque que heroi
            monstro = Ogro("Ogro", vida_monstro, ataque_monstro)

        elif nome_monstro == 'dragao':
            vida_monstro = self.heroi_escolhido.vida*2 #dragao tem o dobro da vida do heroi
            ataque_monstro = self.heroi_escolhido.ataque*1.8 #dragao tem mais 80% ataque que heroi
            monstro = Dragao("Dragao", vida_monstro, ataque_monstro)

        elif nome_monstro == 'caerbannog':
            if self.heroi_escolhido.nome =="ni".lower(): # the knights who say ni!!!
                vida_monstro = 200
                ataque_monstro = 100
            else:
                vida_monstro = self.heroi_escolhido.vida*10 #don't mess with fluffy bunny
                ataque_monstro = self.heroi_escolhido.ataque*50 #don't mess with fluffy bunny
            monstro = Caerbannog("Caerbannog", vida_monstro, ataque_monstro)

        self.monstro_repository.cadastrar_Monstro(monstro)
        print(f"\nMonstro {monstro} com {vida_monstro} de vida e {ataque_monstro} de ataque acordou com o cheiro de comida a fazer!")

    def iniciar_batalha(self):
        heroi = self.heroi_escolhido
        monstro = self.monstro_repository.monstro[-1] #pega o ultimo monstro que foi criado

        print(f"\n{heroi.nome} estava a assar sardinhas com o lume a arder,")
        print(f" encontrou o {monstro.nome} e começou a combater!\n")

        while heroi.vida > 0 and monstro.vida > 0:
            dado_heroi = random.randint(5,20) #turno heroi
            dano_heroi = 0 # inicia dano como 0, porquÊ? não sei...

            if dado_heroi >= 18:
                dano_heroi = dado_heroi*2   # dano critico
                print(f"Ouch, {heroi.nome} fez um ataque crítico")
            elif dado_heroi <= 6:
                dano_heroi = 0 #ataque falhou
                print(f"Oops, {heroi.nome} falhou o alvo... precisas de óculos?")
            else:
                dano_heroi = dado_heroi #ataque normal
                print (f"{heroi.nome} fez {dado_heroi} de dano ao {monstro.nome}")

            monstro.vida -= dano_heroi #tirar vida do monstro subtraindo
            print(f"{monstro.nome} ainda tem {monstro.vida} HP!")

            if monstro.vida <= 0:
                print (f"{monstro.nome} foi derrotado. Yum yum, parece delicioso pensou o {heroi.nome} !!")
                break # batalha termina com derrota do monstro

                    #turno do monstro
            dado_monstro = random.randint(1,12) #dano do monstro
            dano_monstro = dado_monstro
            heroi.vida -= dano_monstro
            print(f"\n{monstro.nome} fez {dado_monstro} de dano a {heroi.nome}")
            print(f"{heroi.nome} ainda sobrevive com {heroi.vida} Hp! \n")

            if self.heroi_escolhido.vida <= 0:
                print(f"{heroi.nome} foi brutalmente e vergonhosamente ANIQUILADO... tipo não restou nada....nada....pelo menos fome já não tem!")
                break # Heroi derrotado

    def regras_regras(self):
        print(f"\n1-  Para equilibrar, não usar um ataque muito altos" )
        print(f"    pois são baseado num d15 (Herói) e num d12 (Monstro);")
        print(f"\n2-  Por exemplo: 150 vida e 30 de ataque;")
        print(f"\n3-  Ao preencher os valores ATK + HP, os mesmos atributos")
        print(f"    são automaticamente concedidos ao monstro;")
        print(f"\n4-  O jogados escolherá apenas se quer lutar contra Ogro ou Dragão;")
        print(f"\n5-  Qualquer semelhança com Dungeons and Dragons é meramente coincidência...")
        print(f"\n6-  ...e também Monty Python and the Holy Grail...just saying..RGPD e cenas...")

menu = Menu()
menu.executar()