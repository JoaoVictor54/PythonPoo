class Pessoa:

    
    def __init__(self,nome="",idade=0):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self,n=1):
        self.idade +=n
        