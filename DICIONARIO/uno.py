

dic = {'jonas': 'jonasreiter@hotmail.com',
       'susan': 'susan.reiter@hotmail.com',
       'Professora': 'contato@reiter.page'}

# print(dic)

# print(dic['susan'])
# print(dic.get('susan'))
# print(dic.get('joão', 'não existe'))
# print(dic.get('gustavo','não existe'))
# dic['Acesso'] = 'entra21@acesso.com.br'
# print(dic)
# dic['Joaquim'] = 'joaquim@gmail.com'
# print(dic)
# print(dic['joaquim'])
# dic['susan'] = 'susan.reiter@hotmail.com'
# print(dic)
# dic.update({'jonas': 'jonas123@hotmail.com'})
# print(dic)
# dic['Professaura'] = dic.pop('Professora')
# print(dic)
# dic['Professaura'] = dic['Professora']
# del dic['Professora']
# print(dic)
# print(dic.values())
# dic.popitem()
# print(dic.values())
# for i in dic:
#        print(i)
#
# for i in dic:
#        print(dic[i])
#
# for k, v in dic.items():
#        print(k,"------",v)
# if 'casimiro' in dic:
#        print('encontrei')
# else:
#        print('Nops')
#
# if 'jonasreiter@hotmail.com' in dic.values():
#        print('encontrei')
# else:
#        print('Nops')

# chaves = ['a', 'b', 'c']
# valor = 0
# novo_dic = dict.fromkeys(chaves, valor)
# print(novo_dic)

lista1 = ['jonas', 'raul', 'stefan']
lista2 = [30, 30, 50]
dic3 = {}
for i in range(len(lista1)):
       dic3[lista1[i]] = lista2[i]
print(dic3)

dic4 = {**dic, **dic3}
print(dic4)

dic.clear()
print(dic)