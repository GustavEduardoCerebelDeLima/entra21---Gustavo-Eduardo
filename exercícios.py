import sqlite3
import requests
import re
# conexao = sqlite3.connect('Banco pokémon do Gustavo.db')
# cursor = conexao.cursor()

# lista = []

# def Criar():
#     cursor.execute('INSERT INTO listapokemon(Nome_pokémon, Tipo_pokémon, Pokedex, Level)'
#                     'VALUES ("Lulu", "Vento",  "983", "1")')
#     conexao.commit()
#
# Criar()

# def Evoluir():
#     cursor.execute('UPDATE listapokemon SET Nome_pokémon="Raichu" WHERE id=1')
#
# Evoluir()

# def Listar():
#     cursor.execute('SELECT * FROM listapokemon[1]')
#     for listapokemon in cursor.fetchall():
#      lista.append(listapokemon[1])
#     print(lista)
#
# Listar()

# def Deletar():
#     cursor.execute('DELETE FROM listapokemon WHERE id=3')
#
# Deletar()

# def Edit():
#     cursor.execute('SELECT * FROM listapokemon')
#     for lista_pokemons in cursor.fetchall():
#         print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')
#     qual = input('Digite o id do pokemon que você quer editar:')
#     linha = input('Digite a opcão que você que editar:\n'
#                   '(1) Nome;\n'
#                   '(2) Tipo;\n'
#                   '(3) Pokedex;\n'
#                   '-')
#     if linha == '1':
#         novonome = input('Digite o novo nome para esse pokemon:')
#         cursor.execute(f'UPDATE lista_pokemons SET nome= "{novonome}" WHERE id="{qual}"')
#
#         cursor.execute('SELECT * FROM lista_pokemons')
#         for lista_pokemons in cursor.fetchall():
#             print(
#                 f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')
#
#
#     elif linha == '2':
#         novotipo = input('Digite o novo nome para esse pokemon:')
#         cursor.execute(f'UPDATE lista_pokemons SET tipo= "{novotipo}" WHERE id="{qual}"')
#
#         cursor.execute('SELECT * FROM lista_pokemons')
#         for lista_pokemons in cursor.fetchall():
#             print(f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')
#
#     elif linha == '3':
#         novapoke = input('Digite o novo numerio para a pokedex:')
#         cursor.execute(f'UPDATE lista_pokemons SET tipo= "{novapoke}" WHERE id="{qual}"')
#
#         cursor.execute('SELECT * FROM lista_pokemons')
#         for lista_pokemons in cursor.fetchall():
#             print(
#                 f'{lista_pokemons[0]} - {lista_pokemons[1]} - {lista_pokemons[2]} - #{lista_pokemons[3]} - {lista_pokemons[4]}')
#
# Edit()

# cursor.execute('SELECT * FROM listapokemon')
# for pokemon in cursor.fetchall():
#     print(f'{pokemon[0]} - {pokemon[1]} - {pokemon[2]} - {pokemon[3]} - {pokemon[4]}')
#
# conexao.commit()
#
# cursor.close()
# conexao.close()

#____________________________________________________________________________________________________________________

# ATVDD 2

conexao = sqlite3.connect('Vendas.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM Clientes')
for cliente in cursor.fetchall():
        print(f'Dados dos clientes/ ID: {cliente[0]} - Nome: {cliente[1]} - CPF: {cliente[2]} - CEP: {cliente[3]} - Cidade: {cliente[4]} - Estado: {cliente[5]} - Rua: {cliente[6]}')
print("-"*50)

cursor.execute('SELECT * FROM produtos')
for produto in cursor.fetchall():
        print(f'Dados dos produto/ ID: {produto[0]} - Codigo de Barras: {produto[1]} - Nome do produto: {produto[2]} - Fabricante do produto: {produto[3]}')
print("-"*50)

cursor.execute('SELECT * FROM vendas')
for legal in cursor.fetchall():
        print(f'Dados das vendas/ ID: {legal[0]} - Data da venda: {legal[1]} - Horario da venda: {legal[2]} - CPF do cliente que comprou: {legal[3]} - Codigo de barras: {legal[4]} - Quantidade: {legal[5]} - Valor Unitario da venda: {legal[6]} - Valor total da venda: {legal[7]}')
print("-"*50)



def Cadastrar():

 while True:

    print()
    op = input('Qual das tabelas você deseja inserir um novo cadastro?\n\n[1]Dados do cliente\n[2]Dados dos produtos\n[3]Dados das vendas\n[4]Ver resultados\nR:')
    print()

    if op == '1':
                nome = input('Digite o nome do cliente: ')
                cpf = input('Digite o cpf do cliente: ')
                entrada = re.findall("\d", cpf)

                if len(cpf) > 14 or len(entrada) < 11 or len(entrada) > 11:
                    print('CPF INVÁLIDO')

                else:
                    valid = 0
                    for dig in range(0, 11):
                        valid += int(entrada[dig])
                        dig += 1
                    if int(entrada[0]) == valid / 11:
                        print("CPF INVÁLIDO")

                    else:
                        soma = 0
                        count = 10
                        for i in range(0, len(entrada) - 2):
                            soma = soma + (int(entrada[i]) * count)
                            i += 1
                            count -= 1
                        dg1 = 11 - (soma % 11)
                        if dg1 >= 10:
                            dg1 = 0

                        soma = 0
                        count = 10
                        for j in range(1, len(entrada) - 1):
                            soma = soma + (int(entrada[j]) * count)
                            j += 1
                            count -= 1
                        dg2 = 11 - (soma % 11)
                        if dg2 >= 10:
                            dg2 = 0

                        if int(entrada[9]) != dg1 or int(entrada[10]) != dg2:
                            print("CPF INVÁLIDO")

                        else:

                            cep = input('Digite o cep do cliente: ')
                            CEP = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
                            cursor.execute(f'INSERT INTO Clientes(nome_cliente, cpf_cliente, cep_cliente, cidade_cliente, estado_cliente, rua_cliente)'
                                            'VALUES(?,?,?,?,?,?)',(nome, cpf, cep,CEP.json()['localidade'],CEP.json()['uf'],CEP.json()['logradouro']))

    elif op == '2':
                cd = input('Digite o codigo do produto: ')
                nome = input('Digite o nome do produto: ')
                fp = input('Digite o fabricante do produto: ')


                cursor.execute('INSERT INTO produtos(codigo_barras, nome_produto, fabricante_produto)'
                               'VALUES(?,?,?)',(cd, nome, fp))

    elif op == '3':
                data = input('Digite a data da venda: ')
                hora = input('Digite a hora do hora: ')
                cpf_cliente = input('Digite o cpf do cliente: ')
                codigo_barra = input('Digite o codigo de barras do produto: ')
                quantidade = input('Digite a quantidade vendida: ')
                valor_unitario = float(input('Digite o valor unitario da venda: '))
                valor_total = float(input('Digite o valor total da venda: '))

                cursor.execute('INSERT INTO vendas(data_venda, hora_venda, cpf_cliente, codigo_barra, quantidade, valor_unitario, valor_total)'
                               'VALUES(?,?,?,?,?,?,?)',(data, hora, cpf_cliente, codigo_barra, quantidade, valor_unitario, valor_total))

    else:
        cursor.execute('SELECT * FROM Clientes')
        for cliente in cursor.fetchall():
            print(f'Dados dos clientes/ ID: {cliente[0]} - Nome: {cliente[1]} - CPF: {cliente[2]} - CEP: {cliente[3]} - Cidade: {cliente[4]} - Estado: {cliente[5]} - Rua: {cliente[6]}')
        print("-" * 50)
        cursor.execute('SELECT * FROM produtos')
        for produto in cursor.fetchall():
            print(f'Dados dos produto/ ID: {produto[0]} - Codigo de Barras: {produto[1]} - Nome do produto: {produto[2]} - Fabricante do produto: {produto[3]}')
        print("-" * 50)
        cursor.execute('SELECT * FROM vendas')
        for legal in cursor.fetchall():
            print(f'Dados das vendas/ ID: {legal[0]} - Data da venda: {legal[1]} - Horario da venda: {legal[2]} - CPF do cliente que comprou: {legal[3]} - Codigo de barras: {legal[4]} - Quantidade: {legal[5]} - Valor Unitario da venda: {legal[6]} - Valor total da venda: {legal[7]}')
        print("-"*50)
        break


def Alterar():
 while True:
    print()
    op = input('Qual das tabelas você deseja alterar?\n\n[1]Dados do cliente\n[2]Dados dos produtos\n[3]Dados das vendas\n[4]Ver tabela\nR:')
    print()


    if op == '1':

        cursor.execute('SELECT * FROM Clientes')
        for cliente in cursor.fetchall():
            print(f'Dados dos clientes/ ID: {cliente[0]} - Nome: {cliente[1]} - CPF: {cliente[2]} - CEP: {cliente[3]} - Cidade: {cliente[4]} - Estado: {cliente[5]} - Rua: {cliente[6]}')

        id = input('Digite a id do cliente que você quer alterar: ')
        print()

        idedit = input('Digite a opcão que você que editar:\n\n(1) Nome do cliente;\n(2) Cpf do cliente;\n(3) Cep do cliente;\nR:')

        if idedit == '1':
                         novonome = input('Digite o novo nome do cliente:')
                         cursor.execute(f'UPDATE Clientes SET nome_cliente= "{novonome}" WHERE id_cliente="{id}"')

        elif idedit == '2':
                         novocpf = input('Digite o novo cpf do cliente:')
                         cursor.execute(f'UPDATE Clientes SET cpf_cliente= "{novocpf}" WHERE id_cliente="{id}"')

        elif idedit == '3':
                         novocep = input('Digite o novo cep do cliente:')
                         cursor.execute(f'UPDATE Clientes SET cpf_cliente= "{novocep}" WHERE id_cliente="{id}"')



    elif op == '2':

        cursor.execute('SELECT * FROM produtos')
        for produto in cursor.fetchall():
            print(f'Dados dos produto/ ID: {produto[0]} - Codigo de Barras: {produto[1]} - Nome do produto: {produto[2]} - Fabricante do produto: {produto[3]}')

        id = input('Digite a id do produto que você quer alterar: ')

        idedit = input('Digite a opcão que você que editar:\n\n(1) Codigo do produto;\n(2) Nome do produto;\n(3) Fabricante do produto;\nR:')
        print()

        if idedit == '1':
                        novonome = input('Digite o novo codigo do produto:')
                        cursor.execute(f'UPDATE produtos SET codigo_barras= "{novonome}" WHERE id_produto="{id}"')

        elif idedit == '2':
                        novocpf = input('Digite o novo nome do produto:')
                        cursor.execute(f'UPDATE produtos SET nome_produto= "{novocpf}" WHERE id_produto="{id}"')

        elif idedit == '3':
                        novocep = input('Digite o novo cep do cliente:')
                        cursor.execute(f'UPDATE produtos SET fabricante_produto= "{novocep}" WHERE id_produto="{id}"')

    elif op == '3':

        cursor.execute('SELECT * FROM vendas')
        for legal in cursor.fetchall():
            print(f'Dados das vendas/ ID: {legal[0]} - Data da venda: {legal[1]} - Horario da venda: {legal[2]} - CPF do cliente que comprou: {legal[3]} - Codigo de barras: {legal[4]} - Quantidade: {legal[5]} - Valor Unitario da venda: {legal[6]} - Valor total da venda: {legal[7]}')

        id = input('Digite a id da venda que você quer alterar: ')
        print()

        idedit = input('Digite a opcão que você que editar:\n\n(1)CPF do cliente;\n(2)Codigo de barras;\n(3)Quantidade\n(4)Valor Unitario\n(5)Valor Total\nR:')
        print()

        if idedit == '1':
                        cpfnovo = input('Digite o novo CPF do cliente:')
                        cursor.execute(f'UPDATE vendas SET cpf_cliente= "{cpfnovo}" WHERE id_cliente="{id}"')

        elif idedit == '2':
                        codbarra = input('Digite o novo codigo de barras:')
                        cursor.execute(f'UPDATE vendas SET codigo_barra= "{codbarra}" WHERE id_cliente="{id}"')

        elif idedit == '3':
                        qtd = input('Digite a nova quantidade de produtos vendidos:')
                        cursor.execute(f'UPDATE vendas SET quantidade= "{qtd}" WHERE id_cliente="{id}"')

        elif idedit == '4':
                        valunit = input('Digite o novo valor unitario da venda:')
                        cursor.execute(f'UPDATE vendas SET valor_unitario= "{valunit}" WHERE id_cliente="{id}"')

        elif idedit == '5':
                        valtot = input('Digite o novo valor total da venda:')
                        cursor.execute(f'UPDATE vendas SET valor_total= "{valtot}" WHERE id_cliente="{id}"')

    else:
        cursor.execute('SELECT * FROM Clientes')
        for cliente in cursor.fetchall():
            print(f'Dados dos clientes/ ID: {cliente[0]} - Nome: {cliente[1]} - CPF: {cliente[2]} - CEP: {cliente[3]} - Cidade: {cliente[4]} - Estado: {cliente[5]} - Rua: {cliente[6]}')
        print("-" * 50)
        cursor.execute('SELECT * FROM produtos')
        for produto in cursor.fetchall():
            print(f'Dados dos produto/ ID: {produto[0]} - Codigo de Barras: {produto[1]} - Nome do produto: {produto[2]} - Fabricante do produto: {produto[3]}')
        print("-" * 50)
        cursor.execute('SELECT * FROM vendas')
        for legal in cursor.fetchall():
            print(f'Dados das vendas/ ID: {legal[0]} - Data da venda: {legal[1]} - Horario da venda: {legal[2]} - CPF do cliente que comprou: {legal[3]} - Codigo de barras: {legal[4]} - Quantidade: {legal[5]} - Valor Unitario da venda: {legal[6]} - Valor total da venda: {legal[7]}')
        print("-"*50)
        break

def Deletar():
    while True:
        print()
        op = input('Qual das tabelas você deseja excluir o registro?\n\n[1]Dados do cliente\n[2]Dados dos produtos\n[3]Dados das vendas\n[4]Ver tabela\nR:')
        print()

        if op == '1':

            cursor.execute('SELECT * FROM Clientes')
            for cliente in cursor.fetchall():
                print(f'Dados dos clientes/ ID: {cliente[0]} - Nome: {cliente[1]} - CPF: {cliente[2]} - CEP: {cliente[3]} - Cidade: {cliente[4]} - Estado: {cliente[5]} - Rua: {cliente[6]}')

            id = input('Digite a id do cliente que você quer excluir: ')
            print()
            cursor.execute(f'DELETE FROM Clientes WHERE id_cliente="{id}"')




        elif op == '2':

            cursor.execute('SELECT * FROM produtos')
            for produto in cursor.fetchall():
             print(f'Dados dos produto/ ID: {produto[0]} - Codigo de Barras: {produto[1]} - Nome do produto: {produto[2]} - Fabricante do produto: {produto[3]}')

            id = input('Digite a id do produto que você quer excluir: ')
            print()
            cursor.execute(f'DELETE FROM produtos WHERE id_produtos="{id}"')


        elif op == '3':

            cursor.execute('SELECT * FROM vendas')
            for legal in cursor.fetchall():
                print(f'Dados das vendas/ ID: {legal[0]} - Data da venda: {legal[1]} - Horario da venda: {legal[2]} - CPF do cliente que comprou: {legal[3]} - Codigo de barras: {legal[4]} - Quantidade: {legal[5]} - Valor Unitario da venda: {legal[6]} - Valor total da venda: {legal[7]}')

            id = input('Digite a id da venda que você quer excluir: ')
            print()
            cursor.execute(f'DELETE FROM vendas WHERE id_venda="{id}"')

        else:
            cursor.execute('SELECT * FROM Clientes')
            for cliente in cursor.fetchall():
                print(f'Dados dos clientes/ ID: {cliente[0]} - Nome: {cliente[1]} - CPF: {cliente[2]} - CEP: {cliente[3]} - Cidade: {cliente[4]} - Estado: {cliente[5]} - Rua: {cliente[6]}')
            print("-" * 50)
            cursor.execute('SELECT * FROM produtos')
            for produto in cursor.fetchall():
                print(f'Dados dos produto/ ID: {produto[0]} - Codigo de Barras: {produto[1]} - Nome do produto: {produto[2]} - Fabricante do produto: {produto[3]}')
            print("-" * 50)
            cursor.execute('SELECT * FROM vendas')
            for legal in cursor.fetchall():
                print(f'Dados das vendas/ ID: {legal[0]} - Data da venda: {legal[1]} - Horario da venda: {legal[2]} - CPF do cliente que comprou: {legal[3]} - Codigo de barras: {legal[4]} - Quantidade: {legal[5]} - Valor Unitario da venda: {legal[6]} - Valor total da venda: {legal[7]}')
            print("-" * 50)
            break

def Listar_vendas_cpf():
     a = input('Digite o cpf que voce quer saber as compras')
     cursor.execute(f'SELECT * FROM vendas WHERE cpf_cliente="{a}"')

def Listar_compras_codigobarras():
     a = input('Digite o codigo de barras do produto que voce quer saber')
     cursor.execute(f'SELECT * FROM vendas WHERE codigo_barras="{a}"')

conexao.commit()
Cadastrar()
Alterar()
Deletar()
Listar_vendas_cpf()

cursor.close()
conexao.close()
