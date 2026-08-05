#criando a classe "o molde"
class Gafanhoto:
    def __init__(self,n="",i= 0): # <--- criando o a função construtora, aquele que guarda atributos
        self.nome = n
        self.idade = i
    # criações dos métodos, "ações que a classe faz"    
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        print(f"O querido(a) gafanhoto(a) se chama {self.nome} e tem {self.idade} ano(s)")


#Criação dos ojetos utilizando como "molde" as classes

g1 = Gafanhoto("andré",12)  # <--- disse que esse obj pertence ao molde gafanhoto

g1.aniversario()
g1.mensagem()

g2 = Gafanhoto("Felipe",16)

g2.mensagem()


g3 = Gafanhoto("Bebê")
g3.idade = 0
g3.aniversario()
g3.mensagem()