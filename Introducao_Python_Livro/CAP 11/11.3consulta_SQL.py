#11.2consulta

import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")#comando select realiza consulta o asterisco representa todos os campos da tabela sendo consultada(nese caso nome e telefone)
resultado = cursor.fetchone()#o methodo fetchone e utilizado para acessar e o resultado do cursor e retorna uma tupla ou None caso a tabela esteja vazia
print("Nome: %s\nTelefone: %s"% (resultado))
cursor.close
conexão.close
