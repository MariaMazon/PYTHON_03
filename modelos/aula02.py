# POLIMORFISMO

class Programa:
    def __init__(self,nome,ano):
        self._nome=nome.title()
        self.ano=ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes+=1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome=nome
        
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.likes}')

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao=duracao    
        
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} - {self.likes}')
        
class Serie(Programa):
    def __init__(self,nome,ano,temporada):
        super().__init__(nome,ano)
        self.temporada=temporada
        
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporada} - {self.likes}')
        
filme1=Filme('Star wars',1977,132)
filme2=Filme('Norbit',2007 ,103)
filme1.dar_likes()
filme2.dar_likes()

# print(f' Nome: {filme1.nome} - Ano: {filme1.ano} - Duração: {filme1.duracao} - Likes: {filme1.likes}')

serie1=Serie('Greys Anatomy',2005,20)
serie2=Serie('Greys Anatomy',2005,16)

serie2.dar_likes()
serie2.dar_likes()

serie1.dar_likes()
serie1.dar_likes()
# print(f' Nome: {serie1.nome} - Ano: {serie1.ano} - Temporada: {serie1.temporada} - Likes: {serie1.likes}')


# 1 CRIANDO UM LIST PARA ARMAZENAR OS OBJETOS 

filmes_e_series=[filme1,serie1]


#ESCREVER UM IF QUE VERIFICA DENTRO DO FOR 
# SE CADA ITERAÇÃO POSSUI DETERMIANDO ATRIBURTO
# for programa in filmes_e_series:
#     detalhes=programa.duracao if hasattr(programa,'duracao') else programa.temporada
#     print(f'{programa.nome} - {programa.ano} - {detalhes} - {programa.likes} ')
    
for programa in filmes_e_series:
    programa.imprime()