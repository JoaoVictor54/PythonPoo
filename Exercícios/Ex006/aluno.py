from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self,nome,idade,turma,curso):
        super().__init__(nome,idade)
        self.turma = turma
        self.curso = curso
    def fazer_matricula(self):
        pass