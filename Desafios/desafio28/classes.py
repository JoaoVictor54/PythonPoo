



class Temperatura:
    def __init__(self):
        self.__temperatura = 24
    


    @property
    def temperatura(self):
        pass
    @temperatura.setter
    def temperatura(self,num):
        if 16 <= num <= 30 and num % 0.5 == 0:
            self.__temperatura = num
        elif num < 16:
            self.__temperatura = 16
        elif num > 30:
            self.__temperatura = 30
        else:
            raise ValueError(f"Bagui tudo errado")
    @property
    def ftemp(self):
        return f"A temperatura atual está {self.__temperatura}°C"