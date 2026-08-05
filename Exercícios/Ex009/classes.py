



class Prova:
    def __init__(self,nome,disciplina):
        self.nome = nome
        self._nota = 0
        self.disciplina = disciplina
    def set_nota(self,num):
        if num >10 or num < 0:
            print("Nota inválida!")
        else:
            self._nota = num
    def get_nota(self):
        return print(f"A nota do aluno {self.nome} em {self.disciplina}: {self._nota:.2f}")