
from rich import print,inspect
from classesex007 import Aluno,Professor

a1 = Aluno("josé",17,"3°A","Ensino Medio")
a1.fazer_aniversario(10)
a1.estudar()
inspect(a1,methods=True)



p1 = Professor("Samuel Cunha",25,"Biologia","mestrado e doutorado")
p1.dar_aula()
p1.estudar()
inspect(p1,methods=True)



