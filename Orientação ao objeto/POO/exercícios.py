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

class Quadrado:

    def __init__(self, tamanholado):
        self.tamanholado = tamanholado

    def __repr__(self):
        return repr(f'{self.tamanholado}')

    def mudarvalor(self):
        self.tamanholado = input('Digite o novo valor: ')

    def retornarvalor(self):
        print(f'O novo valor é {self.tamanholado}')

    def valorarea(self):
        self.tamanholado = tamanholado
        print('O valor de área do quadrado é ', self.tamanholado**2)


q = Quadrado(24)
print(q)
q.mudarvalor()
q.retornarvalor()
print(q)
q.valorarea()




