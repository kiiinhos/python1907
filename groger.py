# def lista_itens(nome,idade,peso):
#     return print(f'{nome},{idade},{peso}')


# nome = 'marcos'
# idade = 25
# peso = 75

# lista_itens(nome,idade,peso)

# def lista_compras(*args): Args ele cria uma lista interna
#     # print(f'lista de comprar de {pessoa}:') possso usar so o *args
#     for item in args:
#      print(item)

# lista_compras('João','frango congelado')
# lista_compras('Maria','sacos de lixo')
# lista_compras('Barbara','cenouras','abacate')

# def lista_compras(**kwargs):
#     fruta = kwargs.get('fruta')
#     if fruta is not None:
#         print(f'Na lista de compras: {fruta}')
    
#     print(f'{kwargs}')

# lista_compras(fruta= 'banana', massas= 'nhoque')
# lista_compras(bebida= ' guarana', sorvete='arroz')

# class Animal:
#     def __init__ (self, nome,dono):
#         self.nome= nome
#         self.dono = dono

#     def comer(self):
#         print(' é nois') 

# class Gato(Animal):
#     def __init__(self,nome,dono,raca):
#         super().__init__(nome, dono)
#         self.raca = raca


#     def miar(self):
#         print('miaaaau')


# class Cachorro(Animal):
#     def latir(self,**kwargs):
#         print('au, auuu')

#         cachorro= Cachorro ('Costela', 'Ipiranga')
#         gato= Gato ('Ajato','Bobao', 'Arroz')

#         print(gato.dono)
        

class Retangulo():
    def __init__(self,largura,comprimento):
        self._largura= largura
        self._comprimento= comprimento

    def getLargura(self):
        return self._largura
    
    def setLargura(self,valor):
        self._largura= valor

    def __add__(self,c):
    print('essa é a largura + comprimento', str(c,largura+c.comprimento))
    return Retangulo(self.largura+ c.largura, self.comprimento + c.comprimento)

    @staticmethod
    def main(*argv):
        print('oi')

c= Retangulo(1,0)
d= Retangulo(2,0)
e= Retangulo(3,0)
        

