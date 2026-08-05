

    
class Contabancaria:
    """Cria uma conta bancária e permite fazer saques e negócios"""
    def __init__(self,id,nome,saldo=0):
        self.id = id
        self._nome =nome
        self.__saldo = saldo
    def __str__(self):
        return(f"A conta {self.id} de {self._nome} contem R$ {self.__saldo:,.2f}")
    
    def depositar(self,valor):
        self.__saldo = abs(self.__saldo)
        self.__saldo += valor
        print(f"deposito de R$ {valor:,.2f} foi autorizado na conta {self.id}")


    def sacar(self,valor):
        self.__saldo = abs(self.__saldo)
        if valor > self.__saldo:
            print(f"Voçê não possui este valor (R$ {valor:,.2f}) para saque")
        else:
            self.__saldo -= valor
            print(f"saque de R$ {valor:,.2f} foi autorizado na conta {self.id}")







