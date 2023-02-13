#11.1exemplo do uso do SQLlite em python

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()#criando um cursor (cursores sãoobjetos utilizados para enviar comandos e receber resultados de dados, eleé criado para uma conexãochamando-se o methodo cursor())
cursor.execute('''create table agenda(nome text, telefone text)''')
cursor.execute('''insert into agenda(nome, telefone)values(?, ?)''',("Nilo", "72565656"))
conexão.commit()
cursor.close()
conexão.close()
