#11.10atualizando o telefone

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("""update agenda set telefone = '1234-5678' where nome = 'Marcos'""")#se tirarmos a clausula where alteramos todos os registros de telefone
conexão.commit()
conexão.close()