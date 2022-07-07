#ATIVIDADE1

import AtividadeDEF as mf

# m1 = float(input("Informe a primeira medida do triângulo: "))
# m2 = float(input("Informe a segunda medida do triângulo: "))
# m3 = float(input("Informe a terceira medida do triângulo: "))
#
# print (mf.batata(m1,m2,m3))

#ATIVIDADE2

# nome = input("Digite qualquer palavra: ")
# print(mf.banana(nome))

#ATIVIDADE3

# num = input("Digite qualquer número: ")
# print(mf.macaca(num))

#ATIVIDADE4

# num = input("Digite qualquer número: ")
# print(mf.banana(num))

#ATIVIDADE 5

from random import randint
import ex5
from time import sleep

ehpedra = False
ehpedra2 = False

for i in range(5):
    # Exibir opções
    ex5.exibir_jogadas()

    while True:
        jog = int(input('Digite sua jogada: '))
        if ehpedra:
            if 2 <= jog <= 3:
                ehpedra = False
                break
        else:
            if 1 <= jog <= 3:
                break

    print(f'Você jogou {ex5.jogada(jog)}')

    # jogada do computador
    if ehpedra2:
        jog2 = randint(2, 3)
        ehpedra = False
    else:
        jog2 = randint(1, 3)

    print(f'PC jogou {ex5.jogada(jog2)}')

    print('JO')
    sleep(0.5)
    print('         KEN')
    sleep(0.5)
    print('                       PO')
    sleep(0.5)


    print(ex5.vencedor(jog, jog2))

    if jog == 1:
        ehpedra = True
    if jog2 == 1: