from rich import print,inspect

class Pessoa:
    
    def __init__(self,nome="",idade=0):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self,n=1):
        self.idade +=n

class aluno(Pessoa):
    def __init__(self,nome,idade,turma,curso):
        super().__init__(nome,idade)
        self.turma = turma
        self.curso = curso
    def fazer_matricula(self):
        pass

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
       super().__init__(nome,idade)
       self.especialidade = especialidade
       self.nivel = nivel
    def dar_aula(self):
        print(f"{self.nome} deu aula")
        

class Secretaria(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor
    def bater_ponto(self):
        pass

a1 = aluno("josé",17,"3°A","Ensino Medio")
p1 = Professor("Samuel Cunha",25,"Biologia","mestrado e doutorado")

a1.fazer_aniversario(10)
p1.dar_aula()



inspect(a1,methods=True)
inspect(p1,methods=True)