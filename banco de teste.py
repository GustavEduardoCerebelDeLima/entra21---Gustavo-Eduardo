import sqlite3
conexao = sqlite3.connect('Banco de dados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'cpf TEXT,'
               'nome TEXT,'
               'data_nascimento TEXT,'
               'cep TEXT,'
               'peso REAL,'
               'altura REAL)')
conexao.commit()
cpf = input('Digite seu CPF: ')
nome = input('Digite seu nome: ')
data_nascimento = input('Digite a data de nascimento: ')
cep = input('Digite o cep: ')
peso = input('Digite o peso: ')
altura = input('Digite a altura: ')

cursor.execute('INSERT INTO clientes(cpf,nome, data_nascimento, cep, peso, altura)'
               'VALUES(?,?,?,?,?,?)',(cpf,nome, data_nascimento, cep, peso, altura))
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for clientes in cursor.fetchall():
    print()
    print(f'{clientes[0]} - {clientes[1]} - {clientes[2]} - {clientes[3]} - {clientes[4]} - {clientes[5]} - {clientes[6]}')

cursor.close()
conexao.close()