from abc import ABC,abstractmethod


class Trasnporte(ABC):
    def __init__(self,distancia,):
        self.distancia = distancia
        
    @abstractmethod
    def cal_frete(self):
        pass



class Moto(Trasnporte):
    def __init__(self, distancia ):
        super().__init__(distancia )
        self.fator = 0.5
    def cal_frete(self):
        self.valor = (self.distancia*self.fator)
        return print(f"O valor do frete da moto em {self.distancia}Km é R$ {self.valor} ")

class Caminhao(Trasnporte):
    def __init__(self, distancia ):
        super().__init__(distancia )
        self.fator = 1.20
    def cal_frete(self):
        self.valor = (self.distancia*self.fator)
        if self.distancia <50:
            return print("A distância deve ser no mínimo 50km!")
        else:
            return print(f"O valor do frete do caminhão em {self.distancia}Km é R$ {self.valor} ")

class Drone(Trasnporte):
    def __init__(self, distancia ):
        super().__init__(distancia )
        self.fator = 9.50
    def cal_frete(self):
        self.valor = (self.distancia*self.fator)
        if self.distancia > 10:
            return print("A distância deve ser no máximo 10km!")
        return print(f"O valor do frete do drone em {self.distancia}Km é R$ {self.valor} ")