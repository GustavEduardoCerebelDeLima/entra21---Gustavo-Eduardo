import sqlite3
conexao = sqlite3.connect('Meu primeiro banco.db')
cursor = conexao.cursor()

# #CRIAR TABELA - C
# cursor.execute('CREATE TABLE IF NOT EXISTS frutas('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nomedafruta TEXT,'
#                'variedade TEXT)')
# CONEXAO.COMMIT()
# #INSERIR DADOS NA TABELA - C
# cursor.execute('iNSERT INTO frutas(nomedafruta, variedade)'
#                'VALUES ("banana","Caturra")')
# conexao.commit()
#ATUALIZAR REGISTRO - U
# cursor.execute('UPDATE frutas SET variedade="BRANCA" WHERE id=3')
# conexao.commit()

#DELETAR - D
# cursor.execute('DELETE FROM frutas WHERE id=1')
# conexao.commit()

# BUSCAR DADOS - R
# cursor.execute('SELECT * FROM frutas')
# for frutas in cursor.fetchall():
#     print(f'{frutas[0]} - {frutas[1]} - {frutas[2]}')

#DELETAR TABELA - D
# cursor.execute('DROP TABLE frutas')
# conexao.commit()

# cursor.close()
# conexao.close()
