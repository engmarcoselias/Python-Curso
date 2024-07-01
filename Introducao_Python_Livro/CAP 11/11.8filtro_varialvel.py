#11.8consulta com filtro de seleção vindo de variavel

import sqlite3

nome = input("Nome a selecionar: ")
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('select * from agenda where nome = "%s"'  % nome)
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s"%(resultado))
cursor.close()
conexão.close()