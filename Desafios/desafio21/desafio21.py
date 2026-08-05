from rich import print


class Caneta:
    def __init__(self,cor):
        if cor == "verde":
            cor = "green"
        elif cor == "vermelho":
            cor = "red"
        elif cor == "azul":
            cor = "blue"
        else:
            cor = "white"
        self.cor = cor
        self.tampa = True
    def destampar(self):
        self.tampa = False
    def tampar(self):
        self.tampa = True
    def escrever(self,frase):
        if self.tampa == True:
            print(f":prohibited: [{self.cor}]Caneta[/] tampada!")
        else:
            print(f"[{self.cor}]{frase}[/]",end="")
            
    def quebrar_linha(self,n):
        for i in range(n):
            print("\n",end="")

c1 = Caneta("verde")
c2 = Caneta("azul")
c3 = Caneta("vermelho")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá gafanhoto, ")
c2.quebrar_linha(0)
c2.escrever("eu gosto desta cor!")
c3.quebrar_linha(1)
c3.escrever("Essa aqui também!")