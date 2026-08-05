from hashlib import sha256
from pwinput import pwinput

class Banco:
    def __init__(self,id,nome,valor,chave = None):
        self._id = id
        self._nome = nome
        self.__valor = valor
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f"A conta {self._id} de {self._nome} foi criada com sucesso, agora possuindo o valor de R${self.__valor:,.2f}")
    def pede_senha(self):
  
        while True:
            senha = str(pwinput("Digite sua senha:"))
            if len(senha) >= 6:
                break
        return senha        



    def depositar(self,n):
        if n >=0:
            self.__valor += n
        else:
            raise ValueError("Valor impossível")
    def sacar(self,n):
        
        if self.validar_senha() == self.__hash:

            if n >= 0:
                print("Saque realizado com Sucesso!")
                self.__valor -= n
            else:
                raise ValueError("Valor impossível")
        else:
            raise PermissionError("Senha incorreta")
    def __str__(self):
        return f"agora a conta de {self._nome} está com R${self.__valor:,.2f} e a senha é {self.__hash}"


    def validar_senha(self):
        txt = str(pwinput("Digite sua senha:"))
        htxt = sha256(txt.encode('utf-8')).hexdigest()
        return htxt

    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,txt):
        if len(txt) > 2 and self.validar_senha() == self.__hash:
            self._nome = txt  
        else:
            print("Senha incorreta ou nome com menos de 3 caracteres!")
        