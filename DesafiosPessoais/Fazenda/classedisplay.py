from classesbases import *
import sys
import os
from time import sleep




# parte que faz loop e faz o uso das classes plantação de animais

class Display:
    def __init__(self):
        self.estado = "home"
        self.estadoescolha = 0
        self.plantacao = Plantacao()
        self.animais = Animais()
        self.painel1 = Panel("[black]1- [orange1]Animais[/]\n2- [green]Plantações[/]\n3- [purple]Status Geral[/]\n4- [red]Sair[/]",title="[yellow]Fazenda[/]",width=30) 
        self.painel2 = Panel("[black]1-[orange1] Ver animais[/]\n2- [orange1]Adicionar animal[/]\n3- [orange1]Alimentar animal[/]")  
        
        self.painel2_1 = Panel(f"{self.animais.status()}")
        #self.painel2_1 = Panel(f"{self.animais.status()} teste de escrite",title="ANIMAIS")
        self.painel2_2 = Panel(f"Qual?(nome):")
        self.painel2_3 = Panel(f"Qual?(por indice)")
        self.painel3 = Panel("[black]1- [green]Ver plantações[/]\n2- [green]Plantar[/]\n3- [green]Regar[/]")
        self.painel3_1 = Panel("")
        self.painel3_2 = Panel("Que plantação? (nome)")
        self.painel3_3 = Panel("qual? (por indice)")


    def status(self):
        print(f"Eu tenho {self.animais.qtanimais} animais com {self.animais.qtalimentado} alimentados e {self.plantacao.qtplantacoes} plantações com {self.plantacao.qtregado} regadas")

    def play(self):
        while True:
            self.desenhar()
            self.escolha()
            os.system('cls' if os.name == 'nt' else 'clear')
            
                


    def desenhar(self):
        if self.estado == "home":
            print(self.painel1)

        if self.estado == "animal":
            print(self.painel2)

            self.estadoescolha = 1
        if self.estado == "animal_1":
            print(self.painel2_1)
            print(str(self.animais.status()))
            self.estado = "home"
            self.desenhar()

        if self.estado == "animal_2":
            print(self.painel2_2)
            self.animais.add(input(":"))
            self.estado = "home"
            self.desenhar()
        if self.estado == "animal_3":
            print(self.painel2_3)
            print(self.animais.status())
            self.animais.alimentar(int(input(":")))
            self.estado = "home"
            self.desenhar()

        if self.estado == "planta":
            print(self.painel3)
            self.estadoescolha = 2


        if self.estado == "planta_1":
            print(self.painel3_1)
            print(self.plantacao.status())
            self.estado = "home"
            self.desenhar()

        if self.estado == "planta_2":
            print(self.painel3_2)
            self.plantacao.add(input(":"))
            self.estado = "home"
            self.desenhar()
        if self.estado == "planta_3":
            print(self.painel3_3)
            print(self.plantacao.status())
            self.plantacao.regar(int(input(":")))
            self.estado = "home"
            self.desenhar()





    def escolha(self):
        n = int(input("---> :"))
        if self.estadoescolha == 0:
            if n == 1:
                self.estado = "animal"
                
            if n == 2:
                self.estado = "planta"
            if n == 3:
                self.status()
                sleep(5)
                
            if n == 4:
                sys.exit()

        if self.estadoescolha == 1:
            if n == 1:
                self.estado = "animal_1"
                self.estadoescolha = 0
                
            if n == 2:
                self.estado = "animal_2"
                self.estadoescolha = 0
            if n == 3:
                self.estado = "animal_3"
                self.estadoescolha = 0


        if self.estadoescolha == 2:
            if n == 1:
                self.estado = "planta_1"
                self.estadoescolha = 0
                        
            if n == 2:
                self.estado = "planta_2"
                self.estadoescolha = 0
            if n == 3:
                self.estado = "planta_3"
                self.estadoescolha = 0
Fazenda = Display()