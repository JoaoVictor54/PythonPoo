from classes import *


def main():
    b1 = Banco(1,"João",12_000,)
    b1.depositar(5000)

    b1.sacar(3000)

    b1.nome = "Victor"
    print(b1)






if __name__ == "__main__":
    main()