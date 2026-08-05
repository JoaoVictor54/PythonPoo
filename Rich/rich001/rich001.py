from rich import print
from rich.table import Table
from rich.panel import Panel

tabela = Table(title="Tabela de preços")
tabela.add_column(header="nome",justify="center",style="white")
tabela.add_column(header="preço",justify="center",style="red")
tabela.add_column(header="quantidade",justify="center",style="white")
tabela.add_row("Banana","R$ 8,00","0")
tabela.add_row("maçã","R$ 4,50","0")
tabela.add_row("pera","R$ 7,00","0")
tabela
print(tabela)


painel = Panel("[green]Senhoras e Senhores![/]",width=25,title="[black]Painel[/]")
print(painel)






print("Hello, [red]World[/red]! ")
print("Olá, pequeno [green on black]gafanhoto[/]! :vulcan_salute:")


print("[red on black] Olá [/]")