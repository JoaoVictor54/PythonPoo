from classes import *

def main():
    

    d1 = Diario("Minecraft")

    d1.escrever("Notch criou o Minecraft, mas isso é segredo")
    d1.escrever("O Herobrine era um hacker irmão do Notch que entrava no mundo dos jogadores")
    d1.escrever("A roupa do Herobrine foi uma tentativa Falha da criação do Steve")
    d1.escrever("Eles fizeram coisas para capturar os sons dos animais morrendo")

    
    #inspect(d1,private=True)


    try:
        d1.ler("Minecraft")

    except Exception as e:
        print(f"[red]Erro: {e}")


if __name__ == "__main__":
    main()