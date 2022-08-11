class Conta:
    def __init__(self, agência, conta, saldo = 0.0):
        self.agência = agência
        self.conta = conta
        self.__saldo = saldo

    def depositar(self,valor):
        self.__saldo += valor
        self.__mensagem()

    def versaldo(self):
        print(self.__saldo)

    def __mensagem(self):
        print(f'Bom dia!, seu deposito foi feito ')


c1 = Conta(3365, '1234-5')
c1.depositar(200)
c1.versaldo()
c1.versaldo()