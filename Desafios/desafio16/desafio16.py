from rich import print
from rich import inspect

class Funcionario:

    empresa = "curso em video"

    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
       return print(f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}")
    



f1 = Funcionario("Maria","Administração","Diretora")
f1.apresentacao()

f2 = Funcionario("Pedro","TI","Programador")
f2.apresentacao()

inspect(f1)
inspect(Funcionario)