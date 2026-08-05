from rich import print,inspect
from classesex005 import Aluno,Professor

a1 = Aluno("josé",17,"3°A","Ensino Medio")
p1 = Professor("Samuel Cunha",25,"Biologia","mestrado e doutorado")

a1.fazer_aniversario(10)
p1.dar_aula()



inspect(a1,methods=True)
inspect(p1,methods=True)