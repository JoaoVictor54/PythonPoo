from rich import print,inspect
from classes import *

a1 = Prova("joao","Matemática")
a1.set_nota(10)
a1.nota = 3
a1.get_nota()

inspect(a1,private=True)