from classes import *

p1 = Mago("Doutor Estranho",1000)
p2 = Guerreiro("Principe Adam",1000)

p1.atacar(p2,500)



print()
print(f"A vida do [green]doutor estranho[/] é HP {p1.vida}")
print(f"A vida do [orange1]principe Adam[/] é HP {p2.vida}")


p2.curar()

p2.atacar(p1,500)

p1.curar()

print()
print(f"A vida do [green]doutor estranho[/] é HP {p1.vida}")
print(f"A vida do [orange1]principe Adam[/] é HP {p2.vida}")