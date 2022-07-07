import requests

# 404 not found
# 200 ok
# 500 internal server error (erro no servidor)
#
# 1XX - Informação
# 2XX - Sucesso
# 3XX - Redirecionar
# 4XX - Erro de cliente (si mesmo)
# 5XX - Erro de servidor

#1

# R = requests.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# print(R.json())
# for i in R.json():
#     if i.upper()[0] == ('S'):
#         print(i, R.json()[i], sep=' - ')

#2
# R = requests.get('https://api-s-38ea2-default-rtdb.firebaseio.com/Escolas.json')
# print(R.json())
# for i in R.json():
#     if len(i) > 14:
#         print(i)
#         print("*Muito grande*")
#         print("")
#     elif len(i) < 8:
#         print(i)
#         print("*Muito pequeno*")
#         print("")
#     else:
#         print(i)
#         print("*Grande*")
#         print("")

#3

# info = '{"Gustavo": "Mengão"}'
# troca = requests.post('https://times-5e780-default-rtdb.firebaseio.com/times/.json', data=info)
# print(troca)

#4

# deletar = requests.delete(f'https://times-5e780-default-rtdb.firebaseio.com/times/Avaí.json')
#
# cores = requests.get('https://cores-d86c6-default-rtdb.firebaseio.com/Cores.json')
#
# cor1 = int(input('01-Azul\n02-Amarelo\n04-Vermelho\n'))
# cor2 = int(input('01-Azul\n02-Amarelo\n04-Vermelho\n'))
#
# if cor1 == cor2:
#     cor = cor1
# else:
#     cor = cor1+cor2
#
# print(cores.json()[cor])

# CEP = requests.get('https://cep.awesomeapi.com.br/json/05424020')
# for i in CEP.json( ):
#     print(CEP.json())

# cep = input("Digite seu CEP: ")
# CEP = requests.get('viacep.com.br/ws//json/ ')
# for i in CEP.json():
#     print(CEP.json())




































































