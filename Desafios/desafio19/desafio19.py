from rich import print
from time import sleep


class Livro:
    def __init__(self,titulo,pagina):
        self.titulo = titulo
        self.paginas = pagina
        self.p = 1
        self.qn = 0
        print(f":open_book:[blue] Você acabou de abrir o livro '[red]{self.titulo}[/]'[blue] que tem [/] [green]{self.paginas} páginas[/][blue] no total. Você está agora na [yellow]página {self.p}[/]")
    def avancar_paginas(self,n):
        self.qn = 0
        while n != 0:
            self.qn += 1
            self.p += 1
            print(f"Pág{self.p} :arrow_right:",end="  ")
            sleep(0.5)
            n -= 1
            if self.p == self.paginas:
                print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")
                break
        print(f"[blue]Você avançou {self.qn} páginas e agora está na[/][yellow] página {self.p}[/]")

l1 = Livro("Diário de um Banana",10)
l1.avancar_paginas(3)
l1.avancar_paginas(7)


l2 = Livro("Sherlock Holmes",50)
l2.avancar_paginas(25)
l2.avancar_paginas(20)
l2.avancar_paginas(100)