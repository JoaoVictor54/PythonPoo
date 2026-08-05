from abc import ABC,abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    inss = 7.5
    salariomin = 1612
    def __init__(self,nome):
        super().__init__()
        self.nome = nome
    @abstractmethod
    def analisar_sal():
        pass



class Horista(Funcionario):
    def __init__(self, nome,v_h,h_t):
        super().__init__(nome)
        self.valor_hora = v_h
        self.horas_trab = h_t
        self.analisar_sal()
    def analisar_sal(self):
        self.sal_bruto = self.valor_hora*self.horas_trab
        self.sal_liq = (self.sal_bruto) - (self.sal_bruto*self.inss/100)
        self.quant_sal = self.sal_liq/self.salariomin
        painel = Panel(f"O salário de [blue]{self.nome}[/blue] [purple]{self.__class__}[/purple] é de [green]R$ {self.sal_liq:.2f}[/green] e corresponde a [yellow]{self.quant_sal:.2f} salários mínimos.[/yellow]",title="Análise de salário",width=55)
        print(painel)



class Mensalista(Funcionario):
    def __init__(self, nome,s_b):
        super().__init__(nome)
        self.sal_bruto = s_b
        self.analisar_sal()
    def analisar_sal(self):
        self.sal_liq = (self.sal_bruto) - (self.sal_bruto*self.inss/100)
        self.quant_sal = self.sal_liq/self.salariomin
        painel = Panel(f"O salário de [blue]{self.nome}[/blue] [purple]{self.__class__}[/purple] é de [green]R$ {self.sal_liq}[/green] e corresponde a [yellow]{self.quant_sal:.2f} salários mínimos.[/yellow]",title="Análise de salário",width=55)
        print(painel)