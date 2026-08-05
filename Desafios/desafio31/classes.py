from rich import inspect
from rich.traceback import install
from abc import ABC,abstractmethod,abstractproperty
install()


class Poligono(ABC):
    def __init__(self):
        asd=asd


   



class Retangulo():
    def __init__(self):
        self._base = 0
        self._altura = 0
        self._area = 0

    @property
    def area(self):
        self._area = self._altura*self._base
        return self._area


    @property
    def base(self):
        pass
    @base.setter
    def base(self,num):
        if num <0 or isinstance(num,str):
            raise ValueError("Valor inválido para base")
        else:
            self._base = num
            
            
    
    @property
    def altura(self):
        pass

    @altura.setter
    def altura(self,num):
        if num < 0 or isinstance(num,str):
            raise ValueError("Valor inválido para base")
        else:
            self._altura = num
            
           
    @property
    def medidas(self):
        return f"a base é {self._base} e altura é {self._altura} e a area é {self.area}"
    @medidas.setter
    def medidas(self,num=(1,1)):
        self.base = num[0]
        self.altura = num[1]
   

    
        

