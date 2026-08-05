from classes import *


def main():
    r = 1
    s1 = Senha()
    s1.senha = "Minecraft"
    print(s1.senha)
    
    while r == 1:
        try:
            s1.validacao(str(input("Digite a senha... : ")))
            r = 0
        except Exception as e:
            print(f"Erro: {e}")
            r = 1




if __name__ == "__main__":
    main()