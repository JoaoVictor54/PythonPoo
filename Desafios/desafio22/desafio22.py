from rich import print
from rich.panel import Panel
import os


class Tv:
    def __init__(self):
        self.ligado = False
        self.volume = 1
        self.canal = 1
        self.escolha = ""
        self.sistema()
        


    def desenhar(self):
        painel_off = Panel(f"[red]:prohibited: A tv está desligada[/red]",title="[ TV ]",width=34)
        painel_on = Panel(f"Canal = {self.canaltxt} \nVolume = {self.volumetxt}",title="[ TV ]",width=34)
        
        if self.ligado == True:
            print(painel_on)
        else:
            print(painel_off)
    def configuração(self) :
        if self.canal == 1:
            self.canaltxt = "[on yellow]1[/] 2 3 4 5"
        elif self.canal == 2 :
            self.canaltxt = "1 [on yellow]2[/] 3 4 5"
        elif self.canal == 3 :
            self.canaltxt = "1 2 [on yellow]3[/] 4 5"
        elif self.canal == 4 :
            self.canaltxt = "1 2 3 [on yellow]4[/] 5"
        elif self.canal == 5 :
            self.canaltxt = "1 2 3 4 [on yellow]5[/]"

        if self.volume == 1:
            self.volumetxt = "[on white][on blue] [/on blue]    [/on white]"
        elif self.volume == 2 :
            self.volumetxt = "[on white][on blue]  [/on blue]   [/on white]"
        elif self.volume == 3 :
            self.volumetxt = "[on white][on blue]   [/on blue]  [/on white]"
        elif self.volume == 4 :
            self.volumetxt = "[on white][on blue]    [/on blue] [/on white]"
        elif self.volume == 5 :
            self.volumetxt = "[on white][on blue]     [/on blue][/on white]"

       


    def controle(self):
        self.escolha = input(f"<Ch{self.canal}>   - Vol{self.volume} + :")
        #print("escolha:"+self.escolha)
        if self.escolha == "@" and self.ligado == False:
            self.ligado = True
        elif self.escolha == "@" and self.ligado == True:
            self.ligado = False
        elif self.escolha == ">" and self.canal != 5:
            self.canal += 1
        elif self.escolha == ">" and self.canal == 5:
            self.canal = 1
        elif self.escolha == "<" and self.canal != 1:
            self.canal -= 1
        elif self.escolha == "<" and self.canal == 1:
            self.canal = 5
        elif self.escolha == "+" and self.volume != 5:
            self.volume += 1
        elif self.escolha == "+" and self.volume == 5:
            self.volume = 5
        elif self.escolha == "-" and self.volume != 1:
            self.volume -= 1
        elif self.escolha == "-" and self.volume == 1:
            self.volume = 1


    def sistema(self):
        
        while self.escolha != "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            self.configuração()
            self.desenhar()
            self.controle()
        os.system('cls' if os.name == 'nt' else 'clear')
       




t1 = Tv()
