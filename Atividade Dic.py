#ATIVIDADE 1

# def aprovacao ():
#    if dic["nota"] >= 7 and dic["nota"] <=10:
#        return("aprovado")
#    elif dic["nota"] >= 10 or dic["nota"] < 0:
#        return("invalido")
#    else:
#        return("reprovado")
#
# dic = {"nome": input("Digite seu nome: "),
#        "nota": float(input("Digite sua nota: "))}
#
# print(dic["nome"])
# print(dic["nota"])
# print(aprovacao())

#ATIVIDADE 2

# from random import randint
# from operator import itemgetter
#
# dic = {}
# for i in range (1,5):
#     dic["jogador", i] = randint(1,6)
#
# dic2 = sorted(dic.items(), key=itemgetter(1), reverse=True)
#
# for j,dic in enumerate(dic2):
#   print(j+1 ," - ", dic2[j])

#ATIVIDADE 3
# def bolinha ():

dic = {"Nome": input("Digite seu nome: "),
       "Carteira trabalho": int(input("Digite sua carteira de trabalho: ")),
       "ano_nasc": int(input("Digite sua idade: "))}

dic["ano_nasc"] = 2022 - dic["ano_nasc"]
print(dic)

if dic["Carteira trabalho"] != 0:
     dic["ano_contr"] = int(input("Digite o ano de nascimento"))
     dic["salário"] = float(input("Digite o salário"))

if dic["Carteira trabalho"] != 0:
     dic["Tempo contrato"] = 2022 - dic["ano_contr"]

print("tempo para aposentadoria: ",90-dic["ano_contr"] - dic["idade"])




#ATIVIDADE 4








