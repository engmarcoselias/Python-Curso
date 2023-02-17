#consulta com filtro de seleção

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda where nome = 'Marcos'")#Apenas acrescentamos a clausula where apos o nome da tabela. O criterio de seleção ou de pesquisadeve ser escrito como uma expressão no caso ex: nome = 'Marcos'
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s"% (resultado))
cursor.close()
conexão.close()