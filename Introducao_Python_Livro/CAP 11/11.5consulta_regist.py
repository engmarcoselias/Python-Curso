#10.5consulta registro por registro

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s"% (resultado))
cursor.close()
conexão.close()