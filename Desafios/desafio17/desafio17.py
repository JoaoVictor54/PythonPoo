from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        fnome = self.nome.center(30,' ')
        fpreco = f"R${self.preco:.2f}"
        painel = Panel(f"{fnome.center(30,' ')}\n{fpreco.center(30,'.')}",title="Produto",width=34,title_align="center",subtitle_align="center")
        print(painel)

p1 = Produto("Iphone Pro Max", 17_150)
p1.etiqueta()
p2 = Produto("mouse", 120)
p2.etiqueta()