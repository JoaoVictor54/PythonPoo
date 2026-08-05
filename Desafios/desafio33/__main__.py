from classes import *
from rich import print
def main():

    a1 = Aluno("João Victor",2008,"Ciência da Computação")
    print(a1.idade)

    #a1.add_curso("Medicina")
    #a1.curso = "Medicina"
    #a1.add_curso("Medicina")

    a1.add_curso("BCC")

    print(f"[green]{a1.nome}[/] nasceu em [blue]{a1.nasc}[/], tem [blue]{a1.idade}[/] anos e agora faz o curso de [purple]{a1.curso}[/]")

    






if __name__ == "__main__":
    main()