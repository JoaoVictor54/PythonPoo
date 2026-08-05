from Ex008 import *

def main():
    c1 = Contabancaria(111,"João",10_000)
    c1.depositar(-100)
    c1.sacar(-100)
    
    print(c1)
    print(c1.__dict__)

    




if __name__ == "__main__":
    main()


    