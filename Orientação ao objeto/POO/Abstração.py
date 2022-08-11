from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, nome, especie, habitat):
#         self.nome = nome
#         self.especie = especie
#         self.habitat = habitat
#
#     # @abstractmethod
#     def pedir_comida(self):
#         return True
#
#     def comer(self):
#         print(f'{self.nome}comeu')
#
#     @staticmethod
#     def nascer():
#         print('nasceu')
#
#     @classmethod
#     def morrer(cls):
#         print('morreu')
#
# class Felino(Animal):
#     def __init__(self, nome, especie, habitat, garras, orelhas):
#         super().__init__(nome, especie, habitat)
#         self.garras = garras
#         self.orelhas = orelhas
#
#     def pedir_comida(self):
#         print('MIAUUUUMMM')

# gatos = Felinos('Milka','Gato','Mato',True,2)
# gatos.pedir_comida()
# Animal.pedir_comida()
# Animal.morrer()
#______________________________________________________________________________________________________________

class Animais(ABC):
    def __init__(self, qtdpatas, cor, corolhos, idade):
        self.qtdpatas = qtdpatas
        self.cor = cor
        self.corolhos = corolhos
        self.idade = idade

    def comer(self):
        print('óia lá ta comendo')

    @abstractmethod
    def andar(self):
        if self.qtdpatas > 0:
         print('óia lá ta andando')
        else:
         print('não anda')

    def piscar(self):
        print('Ele piscaaa')

    def cheirar(self):
        print('Ele cheraaaaaa')

# an = Animais(2, 'Rosa', 'Azul', 2)
# an.andar()

class Felinos(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, tamanhogarras, tamanhopelos):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.tamanhogarras = tamanhogarras
        self.tamanhopelos = tamanhopelos

    def miar(self):
        print('Miau')

    def ronronar(self):
        print('Hnrr hnrr')

    def andar(self):
        print('ele anda finin')

# g = Felinos(4, 'Branca', 'azul', 3, 'Grande', 'fino')
# g.andar()
# g.ronronar()
# g.miar()


class Caninos(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, tamanho, genero):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.tamanho = tamanho
        self.genero = genero

    def andar(self):
        print('ele andou')

    def morder(self):
        print('ROAR aiai meu pé')

    def latir(self):
        print('AUAU')

# c = Caninos(4, 'Branca', 'azul', 3, 'Grandãopae', 'Masculino')
# c.morder()
# c.latir()
# c.andar()



class Reptil(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, rabinho, especie):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.rabinho = rabinho
        self.especie = especie

    def andar(self):
        print('ele andou')

    def lamber(self):
        print('Ele lambe')

    def escalarparede(self):
        print('ELE ESCALOU UMA PAREDE')

# c = Reptil(4, 'Branca', 'azul', 3, 'Cumprido', 'JAré')
# c.lamber()
# c.escalarparede()

class Ovinos(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, la, oqnafamilia):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.la = la
        self.oqnafamilia = oqnafamilia

    def andar(self):
        print('ele andou')

    def baliar(self):
        print('BÉÉÉÉÉÉÉ')

    def coicear(self):
        print('POWW')

# ov = Ovinos(4, 'Branca', 'azul', 3, 'Grande', 'Filhote')
# ov.baliar()
# ov.coicear()

class Peixes(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, tamanhoguelras, cumprimento):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.tamanhoguelras = tamanhoguelras
        self.cumprimento = cumprimento

    def andar(self):
        print('ele andou')

    def nadar(self):
        print('nadano')

    def seescondernacasinhadoaquario(self):
        print('se escondendo')

ov = Peixes(4, 'Branca', 'azul', 3, 'GRANDONAPAE', 18.90)
ov.nadar()
ov.seescondernacasinhadoaquario()
ov.andar()