# print ("TABUADA WHILE!")
# print()
# op = input("deseja ver a tabudada?\nResposta: ")
# print()
#
# while op == "S" or "s":
#   num = int(input("Digite o número desejado: "))
#   print()
#   print(f'{num} x 1 = {num*1}')
#   print(f'{num} x 2 = {num*2}')
#   print(f'{num} x 3 = {num*3}')
#   print(f'{num} x 4 = {num*4}')
#   print(f'{num} x 5 = {num*5}')
#   print(f'{num} x 6 = {num*6}')
#   print(f'{num} x 7 = {num*7}')
#   print(f'{num} x 8 = {num*8}')
#   print(f'{num} x 9 = {num*9}')
#   print(f'{num} x 10 = {num*10}')
#   print()
#   op = input("deseja ver a tabudada?\nResposta: ")
#   print()

# print("ATIVIDADE 4 WHILE")
#
# num = 0
# qt_negativo = 0
# qt_positivo = 0
# maximo = 0
# minimo = 0
# cont = 0
# total = 0
#
# while True:
#     num = int(input("Digite o número desejado, ou 0 para parar: "))
#     if num == 0:
#         break
#         total += num
#         cont += 1
#     if num < 0:
#         qt_negativo += 1
#     else:
#         qt_positivo +=1
#     if num > maximo  or cont == 1:
#         maximo = num
#         minimo = num
#     if num < minimo or cont == 1:
#         minimo = num
#         maximo = num
#
# print("Total lançados: ", total)
# print("Quantidade lançamentos: ", cont)
# print("Média :", total/cont)
# print("Positivos: ", qt_positivo)
# print("Negativos", qt_negativos)
# print(f'porcentagem de positivos: {qt_positvos*100/cont}:.2%')
# print(f'porcentagem de negativos: {qt_negativo*100/cont}:.2%')
# print("Máximo", maximo)
# print("Mínimo", minimo)

bi = 0
pares = 0
ímpares = 0
futuros = 0
passados = 0
bi2 = [0]
pares2 = [0]
ímpares2 = [0]
futuros2 = [0]
passados2 = [0]


ano = int(input("Digite um ano/Quando quiser para digite 0\nResposta: "))
while ano > 0:

    print()
    if ano >= 2022:
     futuros += 1
    else:
     passados += 1
    if ano % 2 == 0:
     pares += 1
    else:
     ímpares += 1
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     bi +=1


    ano = int(input("Digite um ano/Quando quiser para digite 0\nResposta: "))

if ano == 0:

    print("Total de anos pares: ", pares,)
    print("Total de anos ímpares: ", ímpares)
    print("Total de anos futuros: ",futuros)
    print("Total de anos passados: ", passados)
    print("Total de anos bissextos: ", bi)
    print()
    ano = int(input("Digite um ano/Quando quiser para digite 0\nResposta: "))
    print()