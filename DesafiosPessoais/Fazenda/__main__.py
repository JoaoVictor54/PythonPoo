from classes import *

plantacao = Plantacao()
animais = Animais() 

plantacao.add("Plantação de goiba")
plantacao.add("Plantação de jaca")
plantacao.add("Plantação de maça")
plantacao.add("Plantação de uva")

plantacao.regar(1)
#plantacao.regar(2)
plantacao.regar(3)

plantacao.status()

animais.add("Porco")
animais.add("Galinha")
animais.add("Vaca")
animais.add("Ovelha")
animais.alimentar(1)
animais.alimentar(4)
animais.status()
#teste