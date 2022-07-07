# print("OPERAÇÃO - SUBTRAÇÃO!")
#
# num = 1
#
# for i in range(1,4):
#     print(30 * "=")
#     print("CONTA", i)
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite um outro número: "))
#     print("")
#     print(num1, "-", num2, "=", num1 - num2)
#     print("")

# nome = "gustavo"
# for i in nome:
#     print(i)

# num = int(input("Digite algum número: "))
# for i in range(1,num):
#
#  print(i)
#
# num = int(input("Digite algum número: "))
# print('numeros impares: ', end= ' ')
#
# for i in range(num + 1):
#       if i % 2 != 0:
#        print(f'{i}', end= ' ' )


# print ("DUPLAS")
# print("")
#
# M1 = input("Mulher 1: ")
# M2 = input("Mulher 2: ")
# M3 = input("Mulher 3: ")
#
# M4 = [M1,M2,M3]
#
# print("")
# print ("Mulheres: ", M4)
# print("")
#
# M5 = [M1,M2,M3]
#
# H1 = input("Homem 1: ")
# H2 = input("Homem 2: ")
# H3 = input("Homem 3: ")
#
# H4 = [H1,H2,H3]
#
# print("")
# print ("Homens: ", H4)
# print("")
#
#
#
# list([M4.remove(M1)])
# list([M4.remove(M2)])
# list([M4.append(H1)])
#
# list([H4.remove(H1)])
# list([H4.remove(H2)])
# list([H4.append(M1)])
#
# list([M5.remove(M1)])
# list([M5.remove(M3)])
# list([M5.append(H2)])
#
# H5 = M4, H4, M5
#
# for i in (H5):
#  print("Dupla: ", i)

# print("TABUADAS!")
# print("")
# Op = input("Deseja ver uma tabuada? [S ou N]\nResposta: ")
# print("")
# while Op == "S":
#   num = int(input("Tabuada de: "))
#   print("")
#   for i in range(1,11):
#    print(num, "x", i, "=", num*i)
#   print("")
#   Op = input("Deseja ver uma tabuada? [S ou N]\nResposta: ")
#   print("")

# print("CADASTRO DE PRODUTOS!")
#
# n = int(input('Quantos produtos deseja cadastrar?\nResposta:'))
# print()
# print(30*'=')
# print()
# prod = []
# pre = []
# for i in range(n):
#     produto = input(f'Produto {i+1}: ')
#     prod.append(produto)
#     preco = float(input('Preço: R$ '))
#     pre.append(preco)
#     print()
# print(30*'=')
# print()
# for j in range(n):
#     print(f'Produto: {prod[j]} - Preço: R$ {pre[j]}')

# print("ATIVIDADE 5!")
# valor = float(input("Digite o valor a financiar"))
# nper = int(input("Digite a quantidade de parcelas"))
# taxa = float(input("Digite a taxa de juros"))
# opcao = int(input("deseja qual tipo? [1]price [2]SAC"))
#
# if opcao == 1:
#
#  # price
#  #  calcular a parcela
#
#  prestação = valor * (((1+taxa)**nper*taxa)/(1+taxa)**nper)/((1+taxa)**nper-1))
#  print("Nº      Amortização     Juros     Saldo devedor")
#  for i in range(nper):
#   juros = taxa * valor
#   amort = prestação - juros
#   valor -= amort
#   print(i+1,end=' ')
#   print(f'R${prestação:.2f}', end=' ')
#   print(f'R${amort:.2f}', end=' ')
#   print(f'R${juros:.2f}', end=' ')
#   print(f'R${valor:.2f}')
#  #  sac
# elif opcao == 2:
#
#  amort = valor / nper
#
#  for i in range(nper):
#   juros = taxa * valor
#   prestação = amort + juros
#   valor -= amort
#   print(i+1,end=' ')
#   print(f'R$ {prestação:.2f}', end=' ')
#   print(f'R$ {amort:.2f}', end=' ')
#   print(f'R$ {juros:.2f}', end=' ')
#   print(f'R$ {valor:.2f}')
#
# else:
#  print("tu é doente?")
#

# from random import randint
#
# arquivo = open('bananas.txt','r')
# times = arquivo.read().splitlines()
# continuar = "S"
#
# print("FUTEBOL!!!!!!!!!!!!!!!!!!")
#
# while True:
#     pontos = [0] * len(times)
#     cont_casa = 0
#     cont_visita = 0
#     for i in times:
#         for j in times:
#             if i == j:
#                 cont_visita +=1
#                 continue
#             placar_casa = randint(0, 6)
#             placar_visita = randint(0, 6)
#             print(i,"[",placar_casa,"] x [", placar_visita,"]", j)
#             if placar_casa > placar_visita:
#                 pontos[cont_casa] += 3
#             elif placar_visita > placar_casa:
#                 pontos[cont_visita] +=3
#             else:
#                  pontos[cont_casa] +=1
#                  pontos[cont_visita] +=1
#
#             cont_visita += 1
#         cont_visita = 0
#         cont_casa += 1
#
#     print(pontos)
#     maior_point = max(pontos)
#     time_campeão = pontos.index(maior_point)
#
#     print("CAMPEÃO 2022 é o", times[time_campeão], " com ", maior_point, " pontos")
#     ranking = []
#     for i in range(len(times)):
#         ranking.append(f'{pontos[i]} - {times[i]}')
#
#     ranking.sort(reverse=True)
#
#     print()
#     for i in ranking:
#         print(i)
#
#     opcao = input("Deseja continuar?")
#
#     if continuar == "S":
#        continue
#     else:
#         break












