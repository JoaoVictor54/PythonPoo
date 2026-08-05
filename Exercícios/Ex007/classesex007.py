from abc import ABC, abstractmethod #Abstract Base Classes




class Pessoa(ABC):
    def __init__(self,nome="",idade=0):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self,n=1):
        self.idade +=n
    @abstractmethod
    def estudar(self):
        pass    

    
class Aluno(Pessoa):
    def __init__(self,nome,idade,turma,curso):
        super().__init__(nome,idade)
        self.turma = turma
        self.curso = curso
    def fazer_matricula(self):
        pass
    def estudar(self):
        print(f"O aluno {self.nome} esta estudando sobre {self.curso}")

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
       super().__init__(nome,idade)
       self.especialidade = especialidade
       self.nivel = nivel
    def dar_aula(self):
        print(f"{self.nome} deu aula")    

    def estudar(self):
        print(f"O professor {self.nome} esta estudando sobre {self.especialidade}")


class Secretaria(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor
    def bater_ponto(self):
        pass
    def estudar(self):
        return super().estudar()