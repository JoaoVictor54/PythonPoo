from abc import ABC,abstractmethod
from rich import print
import random

class Personagem(ABC):

    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida

    @abstractmethod
    def atacar():
        pass
    def curar():
        pass

class Mago(Personagem):
    ataques = ["[red]bola de fogo![/]","[blue]Geada![/]","[light_yellow]Redemoinhos![/]"]
    def atacar(self,alvo,dano):
        rataque = random.choice(self.ataques)
        rdano = random.randint(0,dano)
        print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/red]({alvo.vida}) com [blue]{rataque}[/] de força {dano}")
        print(f"{alvo.nome} recebeu [red]dano de {rdano}[/]")
        alvo.vida -= rdano
    def curar(self):
        rcura = random.randint(0,100)
        print(f"{self.nome} fez uma magia de cura e [green]recuperou {rcura}HP!")
        self.vida += rcura 
         
class Guerreiro(Personagem):
    ataques = ["[gray]Corte lateral![/]","Ataque com escudo!","Estocada de lamina!"]
    def atacar(self,alvo,dano):
        rataque = random.choice(self.ataques)
        rdano = random.randint(0,dano)
        print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/red]({alvo.vida}) com um [blue]{rataque}[/] de força {dano}")
        print(f"{alvo.nome} recebeu [red]dano de {rdano}[/]")
        alvo.vida -= rdano
    def curar(self):
        rcura = random.randint(0,100)
        print(f"{self.nome} passou uma atadura no braço e [green]recuperou {rcura}HP!")
        self.vida += rcura  

