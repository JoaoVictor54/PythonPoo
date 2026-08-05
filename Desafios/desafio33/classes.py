from abc import ABC



class Pessoa(ABC):
    def __init__(self,nome,nasc):
        self.__nome = nome
        self.__nasc = nasc

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,n):
        print("Não é permitido a troca de nome!")


    @property
    def nasc(self):
        return self.__nasc
    @nasc.setter
    def nasc(self,n):
        print("Não é permitido a troca da data de nascimento!")

    @property
    def idade(self):
        calc_idade = 2026-self.__nasc
        return calc_idade
    @idade.setter
    def idade(self,n):
        print("Não é permitido a troca da idade!")






class Aluno(Pessoa):
    def __init__(self,nome,nasc,curso):
        super().__init__(nome,nasc)
        self.__curso = curso
        self._cursos =["ADS","ADM","BCC","LCC","Ciência da Computação"]
        if curso not in self._cursos:
            raise ValueError("Curso não disponível")

    def add_curso(self,n):
        if n not in self._cursos:
            print(f"Curso {n} adicionado com sucesso!")
            self._cursos.append(n)
        else:
            print(f"O Curso já existe na lista de cursos oficiais!")
            

    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self,n):
        if n in self._cursos:
            print(f"Troca de curso para {n} Bem sucedida!")
            self.__curso = n
        else:
            print(f"Curso {n} não está no banco de cursos válidos!")



    
         
   
    

    

     