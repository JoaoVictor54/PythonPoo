

    
class Contabancaria:
    """Cria uma conta bancária e permite fazer saques e negócios"""
    def __init__(self,id,nome,saldo=0):
        self.id = id
        self.nome =nome
        self.saldo = saldo
    def __str__(self):
        return(f"A conta {self.id} de {self.nome} contem R$ {self.saldo:,.2f}")
    
    def depositar(self,valor):
        self.saldo += valor
        print(f"deposito de R$ {valor:,.2f} foi autorizado na conta {self.id}")


    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Voçê não possui este valor (R$ {valor:,.2f}) para saque")
        else:
            self.saldo -= valor
            print(f"saque de R$ {valor:,.2f} foi autorizado na conta {self.id}")


c1 = Contabancaria(122,"João",3000)

c1.depositar(100)
c1.sacar(50000)
print(c1)




