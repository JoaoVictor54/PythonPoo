from abc import ABC,abstractmethod

class Gerenciamento(ABC):
    def __init__(self):
        self.__quantSlots = 0

    @abstractmethod
    def status(self):
        pass
    @abstractmethod
    def add(self,nome):
        pass





class Plantacao(Gerenciamento):
    def __init__(self):
        self.qtplantacoes = 0
        self.qtregado = 0
        self.totalplantacoes = []
        self.seregado = []


    def status(self):
        print(f"Eu tenho {self.qtplantacoes} Plantações e {self.qtregado} foram regadas\n")
        n=1
        for i in self.totalplantacoes:
            print(f"{n}- {i} {self.seregado[n-1]} ")
            n+=1
            


    def add(self,nome):
        self.totalplantacoes.append(nome)
        self.seregado.append("(Não regado)")
        self.qtplantacoes +=1


    def regar(self,i):
        self.seregado[i-1] = "(Regado)"
        self.qtregado +=1



class Animais(Gerenciamento):
    def __init__(self):
        self.totalanimais = []
        self.sealimentado = []


    def status(self):
        print("Eu tenho Tantos animais e Tantas foram alimentados")
        print("Quantidade de animais e quantos foram aimentados ")


    def add(self,nome):
        self.totalanimais.append(nome)
        self.sealimentado.append("Não alimentado")


    def alimentar(self,i):
        self.sealimentado[i-1] = "Alimentado"