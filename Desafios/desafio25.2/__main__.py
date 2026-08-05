from rich import print
from rich.table import Table


def main():

    dist=100



    valormoto = 0.50*(dist)
    valorcaminhao = 1.20*(dist)
    valordrone = 9.50*(dist)

    tabela = Table(title= "Tabela de fretes")
    tabela.add_column(header="Distância",justify="center",style="white")
    tabela.add_column(header="Tipo",justify="center",style="white")
    tabela.add_column(header="Frete",justify="center",style="white")
    tabela.add_row(f"{dist}Km","Moto",f"R$ {valormoto:.2f}")


    #Caminhão
    if dist < 50:
        tabela.add_row(f"{dist}Km","Caminhao","Distância mínima (50km) não atingida")
    else:
        tabela.add_row(f"{dist}Km","Caminhao",f"R$ {valorcaminhao:.2f}")

    #Drone
    if dist >10:
        tabela.add_row(f"{dist}Km","Drone","Distância máxima (10Km) ultrapassada")
    else:
        tabela.add_row(f"{dist}Km","Drone",f"R$ {valordrone:.2f}")



    print(tabela)





if __name__ == "__main__":
    main()