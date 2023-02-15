#11.3inserindo multiplos registros

import sqlite3

dados = [("joão", "92242588"),("andre", "995656565"),("Marcos","96591999991")]
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.executemany('''insert into agenda(nome, telefone)values(?,?)''', dados)
conexão.commit()
cursor.close()
conexão.close()