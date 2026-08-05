from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Churrasco:
    def __init__(self,titulo,quant):
        self.titulo = titulo
        self.quant = quant
    def analise(self):
        rec = 0.4 * self.quant 
        cust = rec*82.40
        pag = cust/self.quant
        painel = Panel(f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\nCada convidado comerá 0.4kg e cada kg custa R$ 82.40\nRecomendo [blue]comprar {rec:.2f}kg[/] de carne\nO custo total será de [green]R${cust:.2f}[/]\nCada pessoa pagará [yellow]R${pag}[/] para participar.",title=(f"{self.titulo}"),width=60)
        return print(painel)
    
c1 = Churrasco("Churras dos Amigos",15)
c1.analise()

c2 = Churrasco("Churrasco da pelada",20)
c2.analise()

c3 = Churrasco("Churrasco da familia",78)
c3.analise()