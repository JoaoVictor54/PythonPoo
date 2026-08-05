from abc import ABC,abstractmethod
from rich import print

class Poligono(ABC):
    def __init__(self,lados):
        self.vl_lados=lados
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass



class Quadrado(Poligono):
    def __init__(self,lados):
        super().__init__(lados)
    def perimetro(self):
        valor=(self.vl_lados*4)
        return print(f"Perimetro = {valor:.1f}")
    def area(self):
        valor = (self.vl_lados**2)
        return print(f"Area = {valor:.1f}")

class Circulo(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
    def area(self):
        valor=3.14*(self.vl_lados**2)
        return print(f"Area = {valor:.1f}")
    def perimetro(self):
        valor = 3.14*(self.vl_lados*2)
        return print(f"Perimetro = {valor:.1f}")