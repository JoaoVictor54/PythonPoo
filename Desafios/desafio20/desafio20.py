from rich import print  
from rich.panel import Panel

class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    def add_favoritos(self,jogo):
        self.jogos.append(f":video_game:  [blue]{jogo}[/]\n")
        self.jogos.sort()
    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]\nJogos favoritos: \n"
        for i in self.jogos:
            conteudo += i
        painel = Panel(conteudo,title=f"Jogador <{self.nick}>",width=35)
        print(painel)


g1 = Gamer("João Victor", "Tripa Seca")
g1.add_favoritos("Minecraft")
g1.add_favoritos("Cs 1.6")
g1.add_favoritos("Roblox")
g1.add_favoritos("Katana Zero")
g1.add_favoritos("Punch Club")
g1.ficha()


g2 = Gamer("Felipe","Racha Cuca")
g2.add_favoritos("Cs 1.6")
g2.add_favoritos("Cs2")
g2.ficha()