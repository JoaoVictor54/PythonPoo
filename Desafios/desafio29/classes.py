from rich import print
from rich import inspect

class Diario:
    def __init__(self,senha="admin123"):
        self.__senha = senha
        self.conteudo = []

    def escrever(self,text):
        self.conteudo.append(text)
        
    def ler(self,text=""):
        if text == self.__senha:
            print(f"[green]Senha correta, Diário liberado para leitura![/]\n")
            for i in self.conteudo:
                print(f"{i}\n")
        else:
            raise PermissionError(f"[red]Senha incorreta, Você não tem acesso ao diário![/]")

    @property
    def senha(self):
        return "Fela da mãe, você não permissão de ver a senha! :-| "