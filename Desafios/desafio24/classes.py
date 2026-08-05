from abc import ABC, abstractmethod


class BebidasQuentes(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print("--- Iniciando Bebida ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---\n\n")

    def ferver_agua(self):
        print("Passo 1: Esquentando a água até 100 graus celcius")
        self.misturar()

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidasQuentes):
    def misturar(self):
        print("Passo 2: Colocando o pó de café na água quente")
        
    def servir(self):
        print("Passo 3: Servindo o Café com o Açucar ao lado")
        

class Cha(BebidasQuentes):
    def misturar(self):
        print("Passo 2: Colocando as folhas do chá na água quente")
        
    def servir(self):
        print("Passo 3: Servindo o Chá com o açucar ao lado")
        

class Leite(BebidasQuentes):
    def misturar(self):
        print("Passo 2: Colocando o pó do leite na água")
        
    def servir(self):
        print("Passo 3: Servindo o leite com o açucar ao lado")
        


def q():
    print()