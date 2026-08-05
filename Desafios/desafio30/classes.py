from hashlib import sha256
from rich import print

class Senha:
    def __init__(self):
        self.__senhahash = 'x'
    @property
    def senha(self):
            return self.__senhahash
    @senha.setter
    def senha(self,text):
        htext = sha256(text.encode('utf-8')).hexdigest()
        self.__senhahash = htext

    def validacao(self,text):
        htext = sha256(text.encode('utf-8')).hexdigest()
        if htext == self.__senhahash:
            print("[green]Senha Validada")
        else:
            raise PermissionError("[red]Senha Incorreta")