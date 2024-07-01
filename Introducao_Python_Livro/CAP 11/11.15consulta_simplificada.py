#11.14consulta varios registros, acesso simplificado

import sqlite3

with sqlite3.connect("agenda.db") as conexão:
    for registro in conexão.execute("select * from agenda"):
        print("Nome: %s\nTelefone: %s"%(registro))