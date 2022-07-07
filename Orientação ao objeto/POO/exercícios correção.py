class Lata:
    def __init__(self, altura, diametro, volume, material='aluminio', rotulo='coca'):
        self.altura = altura
        self.diametro = diametro
        self.volume = volume
        self.material = material
        self.rotulo = rotulo
        self.lacre = True
        self.amassada = False
        self.descartada = False
        self.aberta = False

    def abrir(self):
        if self.aberta:
            print('já está aberta, bocó')
        else:
            print('Lata foi aberta com sucesso')
            self.aberta = True

    def beber(self, quantidade):
        if not self.aberta:
            print('Lata ainda está fechada')
        elif quantidade > self.volume:
            print(f'Você bebeu {self.volume}, e ainda faltou {quantidade-self.volume}')
            self.volume = 0
        else:
            self.volume -= quantidade
            print(f'Você bebeu {quantidade}, e na lata ainda resta {self.volume}')

    def esvaziar(self):
        if not self.aberta:
            print('Não dá pra esvaziar com a lata fechada')
        else:
            print('Lata vazia')
            self.volume = 0

    def amassar(self):
        if not self.amassada and self.volume == 0:
            print('Lata amassada')
            self.amassada = True
        else:
            print('Não dá pra amassar')

    def retirar_lacre(self):
        if self.lacre:
            self.lacre = False
            print('Lacre retirado')
        else:
            print('Não tinha lacre')

    def descartar(self):
        if self.descartada:
            print('Não pode descartar o que já está descartado')
        elif self.amassada:
            print('Descartada no lixeiro amarelo')
            self.descartada = True
        else:
            print('Primeiro, amasse a lata')


l1 = Lata(12.22, 5.2, 350)
l1.abrir()
l1.beber(300)
l1.descartar()
l1.esvaziar()
l1.amassar()
l1.retirar_lacre()
l1.amassar()
l1.descartar()

