#ATVDD da 1 a 4

# velho = open('clientes sistema antigo.txt', 'r').read().splitlines()
# novo = open('clientes sistema novo.txt', 'r').read().splitlines()
#
# print(len(velho + novo))
# nova_lista =set(velho + novo)
# print(len(nova_lista))
#
# old = open('clientes sistema antigo.txt', 'r').read().splitlines()
# new = open('clientes sistema novo.txt', 'r').read().splitlines()
#
# total_list = old + new
# cont = 0
#
#
# velho = open('clientes sistema antigo.txt', 'r').read().splitlines()
# novo = open('clientes sistema novo.txt', 'r').read().splitlines()
#
# total = velho + novo
#
# D = set()
# for i in total:
#     if total.count(i) > 1:
#         D.add(i)
#
# print(len(D))
#
# print(f'Duplicados {D}')
#
#
#
# set1 = set(velho + novo)
# print(len(set1))

# ==============================================================================

a = open('Candidato A.txt', 'r').read().splitlines()
b = open('Candidato B.txt', 'r').read().splitlines()

a1 = set(a)
b1 = set(b)

print("Total de votos: ", len(a + b))
print("Votos do candidato A: ", len(a))
print("Votos do candidato B: ", len(b))

if len(a) == len(b):
    print('Quem ganhou? : Empate')

laa = a1.intersection(b1)
print("Pessoas que votaram nos 2  candidatos: ",len(laa))

print("Candidato A:", len(a1), "e candidato B:", len(b1))

vala = 108 - len(set(a).intersection(set(b)))
print(vala, "pessoas votaram e", 100 - vala ,"não votaram")








