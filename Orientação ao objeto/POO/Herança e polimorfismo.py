class Veiculo:

    def __init__(self, cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo):
        self.cor = cor
        self.lugares = lugares
        self.qntpneus = qntpneus
        self.tipomotor = tipo_motor
        self.valor = valor
        self.ano = ano
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print('acelerou')

    def freiar(self):
        print('freiou')

    def ligar(self):
        print('ligou')

    def desligar(self):
        print('desligou')

class Moto(Veiculo):
    def __init__(self, cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo, empinada=False):
        super().__init__(cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo)
        self.empinada = empinada

    def empinar(self):
        if self.empinada:
            print('Ja ta empinada maluko')
        else:
            print('IMPINA')
            self.empinada = True

    def desempinar(self):
        self.empinada = False
        print('desempinou')

# m1 = Moto('Azul', 2, 2, '125', 17000, 2022, 'Honda','CG-125',True)
# m1.empinar()
# m1.desempinar()

class Carro(Veiculo):
    def __init__(self, cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo,janelas = False ,portas = False):
        super().__init__(cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo)
        self.portas = portas
        self.janelas = janelas

    def abaixarjanelas(self):
        if self.janelas:
            print('A janela ja tá abaixada')
        else:
            print('Abaixei a janela')
            self.janelas = True

    def subirjanelas(self):
            print('Subi a janela')
            self.janelas = False

    def abrirportas(self):
        if self.portas:
            print('A porta ja ta aberta')
        else:
            print('Abri a porta')
            self.porta = True

    def fecharportas(self):
            print('Fechei a porta')
            self.porta = False

# c1 = Carro('Azul', 2, 2, '125', 17000, 2022, 'Honda','CG-125' ,False ,False)
# c1.abaixarjanelas()
# c1.subirjanelas()
# c1.abrirportas()
# c1.fecharportas()

class Onibus(Veiculo):
    def __init__(self, cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo, lotado = False ,portonas=False):
        super().__init__(cor, lugares, qntpneus, tipo_motor, valor, ano, marca, modelo)
        self.lotado = lotado
        self.portonas = portonas

    def taounlotado(self):
        if self.lotado:
            print('Onibus lotado, n para no próximo ponto')
        else:
            print('Onibus ainda n ta lotado, para no próximo ponto')
            self.lotado = True

    def abrirportonas(self):
        if self.portonas:
            print('Portona ta aberta já')
        else:
            print('Abrindo portona')
            self.portonas = True

    def fecharportonas(self):
            print('Fechando portona')
            self.portonas = False

# o1 = Onibus('Amarelo', 2, 2, '125', 17000, 2022, 'Honda','CG-125' ,False ,False)
# o1.taounlotado()
# o1.taounlotado()
# o1.abrirportonas()
# o1.abrirportonas()
# o1.fecharportonas()
# o1.fecharportonas()

class Animais:
    def __init__(self, qtdpatas, cor, corolhos, idade):
        self.qtdpatas = qtdpatas
        self.cor = cor
        self.corolhos = corolhos
        self.idade = idade

    def comer(self):
        print('óia lá ta comendo')

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

# g = Felinos(4, 'Branca', 'azul', 3, 'Grande', 'fino')
# g.ronronar()
# g.miar()


class Caninos(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, tamanho, genero):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.tamanho = tamanho
        self.genero = genero

    def morder(self):
        print('ROAR aiai meu pé')

    def latir(self):
        print('AUAU')

# c = Caninos(4, 'Branca', 'azul', 3, 'Grandãopae', 'Masculino')
# c.morder()
# c.latir()

class Reptil(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, rabinho, especie):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.rabinho = rabinho
        self.especie = especie

    def lamber(self):
        print('Ele lambe')

    def escalarparede(self):
        print('ELE ESCALOU UMA PAREDEEEEE')

# c = Reptil(4, 'Branca', 'azul', 3, 'Cumprido', 'JAré')
# c.lamber()
# c.escalarparede()

class Ovinos(Animais):
    def __init__(self, qtdpatas, cor, corolhos, idade, la, oqnafamilia):
        super().__init__(qtdpatas, cor, corolhos, idade)
        self.la = la
        self.oqnafamilia = oqnafamilia

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

    def nadar(self):
        print('nadano')

    def seescondernacasinhadoaquario(self):
        print('se escondendo'
              '')

ov = Peixes(4, 'Branca', 'azul', 3, 'GRANDONAPAE', 18.90)
ov.nadar()
ov.seescondernacasinhadoaquario()


