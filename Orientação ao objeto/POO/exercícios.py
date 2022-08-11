# Criar uma classe para uma lata de coca-cola.
# A classe deve ter todos os atributos dimensionais,
# e suas características de material.
# As funcionalidades(métodos) da lata sao, abrir,
# beber, esvaziar, amassar, retirar lacre, e descartar

# class Lata:
#     def __intit__(self, altura, diametro, volume, material, rotulo):
#         self.altura = altura
#         self.diametro = diametro
#         self.volume = volume
#         self.material = material
#         self.rotulo = rotulo
#
#     def __repr__(self):
#         return repr(f'{self.altura} - {self.diametro} - {self.volume} - {self.material} - {self.rotulo}')
#
#     def abrir(self):
#         print(f'TSchhhhk *abriu a lata da {self.rotulo}')
#
#     def beber(self):
#         print(f'GLUBGLUB *bebeu o liquido {self.rotulo}')
#
#     def esvaziar(self):
#         print(f'glugluglulguglu *esvaziou a lata da {self.rotulo}')
#
#     def amassar (self):
#         print(f'BLAM *amassou a lata da {self.rotulo}')
#
#     def descartar(self):
#         print(f'flupt *descartou a lata da {self.rotulo}')

#Atividade1

# class Bola:
#
#     def __init__(self, cor, circunferencia, material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material
#
#     def __repr__(self):
#         return repr(f'{self.cor} - {self.circunferencia} - {self.material}')
#
#     def trocaCor(self):
#        self.cor = input('Digite a nova cor para a bola: ')
#
#
#     def mostraCor(self):
#         print(f'A cor da bola é {self.cor}')
#
# v1 = Bola('Branco', '48cm e 78cm', 'couro sintètico')
# print(v1)
# print()
# v1.trocaCor()
# v1.mostraCor()
# print()
# print(v1)

#Atividade2

# class Quadrado:
#
#     def __init__(self, tamanholado):
#         self.tamanholado = tamanholado
#
#     def __repr__(self):
#         return repr(f'{self.tamanholado}')
#
#     def mudarvalor(self):
#         self.tamanholado = int(input('Digite o novo valor: '))
#
#     def retornarvalor(self):
#         print(f'O novo valor é {self.tamanholado}')
#
#     def valorarea(self):
#
#         print(f'O valor da área do quadrado é {self.tamanholado**self.tamanholado}')
#
#
# q = Quadrado(34)
# print(q)
# q.mudarvalor()
# q.retornarvalor()
# print(q)
# q.valorarea()

#Atividade3

# class Retangulo:
#     def __init__(self, comprimento, largura):
#         self.comprimento = comprimento
#         self.largura = largura
#
#     def __repr__(self):
#         return repr(f'{self.comprimento} - {self.largura}')
#
#     def mudarvalor(self):
#         print()
#         self.comprimento = int(input('Digite um novo valor de comprimento: '))
#         self.largura = int(input('Agora, um novo valor de largura: '))
#
#     def retornarvalor(self):
#         print()
#         print(f'O valor do comprimento é {self.comprimento}')
#         print(f'E o valor da largura é {self.largura}')
#
#     def calculararea(self):
#         print()
#         print(f'O valor da área do retangulo é {self.comprimento**self.comprimento}')
#
#     def calcularperimetro(self):
#         print()
#         print(f'O valor do perimetro do retangulo é {self.largura ** self.largura}')
#
# r = Retangulo(2,3)
# r.retornarvalor()
# r.mudarvalor()
# r.retornarvalor()
# r.calculararea()
# r.calcularperimetro()

#Atividade 4

# class Combustivel:
#
#     def __init__(self, tipocombustivel, valorlitro, qtdcombustivel):
#         self.tipocombustivel = tipocombustivel
#         self.valorlitro = valorlitro
#         self.qtdcombustivel = qtdcombustivel
#
#     def __repr__(self):
#         return repr(f'{self.tipocombustivel} - {self.valorlitro} - {self.qtdcombustivel}')
#
#     def abastecerporvalor(self):
#         valor = float(input('Digite o valor desejado para abastecer: '))
#         toptop = self.valorlitro
#         tot = valor/toptop
#         print(f'A quantidade será de {tot} litro')
#
#     def abastecerporlitro(self):
#         ama = float(input('Digite a quantidade desejado para abastecer: '))
#         top = self.valorlitro
#         tot = ama*top
#         print(f'Irá custar {tot} R$')
#
#     def alterarvalor(self):
#         self.valorlitro = float(input('Digite o novo preço do combustivel: '))
#         print(f'O combustível agora está custando {self.valorlitro}R$')
#
#     def alterarcombustivel(self):
#         self.tipocombustivel = input('Digite o novo tipo do combustivel: ')
#         print(f'Agora o combustivel que vendemos é o {self.tipocombustivel}')
#
#     def alterarquantidadecombustivel(self):
#         self.qtdcombustivel = input('Digite a quantidade de combustivel na bomba: ')
#         print(f'A quantidade de combustivel na bomba é{self.qtdcombustivel}')
#
#
# inf = Combustivel('Etanol' ,7.30 ,200)
# inf.abastecerporlitro()
# print()
# inf.abastecerporvalor()
# print()
# print(inf)
# print()
# inf.alterarvalor()
# print()
# inf.alterarcombustivel()
# print()
# inf.alterarquantidadecombustivel()
# print(inf)

#Atividade5
# contador = 0
# class Macaco:
#     def __init__(self, nome, bucho):
#         self.nome = nome
#         self.bucho = bucho
#
#     def comer(self):
#      comida = input('O que você quer que o macaco coma? ')
#      print('O macaco comeu', comida)
#      contador + 1
#         if contador > 3:
#          print('O macaco ta cheio,para')
#
#     def verbrucho(self):
#         print('o macaco tem no bucho', self.comer)
#
#     def digerir(self):
#         print('UMACACUCAGO')
#
# M = ('Cesar', 'Vazio')
# M.comer






#Atividade8

# class Fusca:
#     def __init__(self, consumodecombustivel, combustivelnotanque):
#         self.consumodecombustivel = consumodecombustivel
#         self.combustivelnotanque = combustivelnotanque
#
#     def __repr__(self):
#         return repr(f'{self.consumodecombustivel} - {self.combustivelnotanque}')
#
#     def andar(self):



