#ATIVIDADE1

# def batata(m1,m2,m3):
#
#  if m1 == m2 and m1 == m3 and  m2 == m3:
#     return print("Seu triângulo é um Equilátero.")
#
#  elif m1 > m2+m3 or m2 > m1+m3 or m3 > m1+m2:
#     return print("Isso não é um triângulo.")
#
#  elif m1 != m2 and m1 == m3 and m3 != m2 or m1 == m2:
#     return print("Seu triângulo é um isósceles.")
#
#  else:
#     return print("Seu triângulo é um Escaleno.")

# ATIVIDADE2

# def banana(nome):
#     cont = 0
#     for i in nome:
#         cont +=1
#         pass
#     return cont


#ATIVIDADE3

# def macaca(num):
#     return num[::-1]

#ATIVIDADE4

# def banana(num):
#     cont = 0
#     for i in num:
#         cont+=1
#         pass
#     return cont

#ATIVIDADE 5

# import random
# import time
# wins = 0
# def bolacha(esc,winsinim,wins):
#
#
#  while True:
#     esc = esc.upper()
#     jokenpo = "PEDRA", "PAPEL", "TESOURA"
#     bot = random.choice(jokenpo)
#     time.sleep(0.5)
#     print("…JO……KEN……PO……")
#     time.sleep(1)
#     print()
#     print("O bot escolheu: ", bot)
#     if esc == bot:
#      print("EMPATE!")
#      time.sleep(3)
#      print()
#     elif esc == "PEDRA" and bot == "PAPEL" or esc == "PAPEL" and bot == "TESOURA" or esc == "TESOURA" and bot == "PEDRA":
#      print("você perdeu!")
#      time.sleep(3)
#      print()
#      winsinim += 1
#     else:
#      print("Você ganhou!")
#      time.sleep(3)
#      print()
#      wins += 1
#     while True:
#      if wins < 2 or winsinim < 2:
#       break
#      else:
#       print("FIM DE JOGO RESULTADOS: INIMIGO = ", winsinim, "/VOCÊ = ", wins)
#      win = wins
#      wininim = winsinim

# fazer a jogada
# validar a jogada
# fazer a jogada do pc
# verificar o vencedor
# fazer o JO...KEN...PO

def exibir_jogadas():
    print("""Escolha sua jogada
[1] - Pedra
[2] - Papel
[3] - Tesoura""")


def jogada(n):
    if n == 1:
        return 'Pedra'
    elif n == 2:
        return 'Papel'
    else:
        return 'Tesoura'


def vencedor(a, b):
    if a == b:
        return 'Empate'
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        return 'Vitoria da máquina'
    else:
        return 'Vitória sua'







