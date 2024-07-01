#consultando multiplos resultados

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor  = conexão.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall()#o methodo fetchall retorna uma lista de tuplas(é interessante para consultas menores)fetch = obter all = todos
for registro in resultado:
    print("Nome: %s\nTelefone: %s"% (registro))
cursor.close()
conexão.close()