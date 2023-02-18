#11.11exemplode update sem where e com rowcount

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("""update agenda set telefone ='1111-1111' """)
print("Registros alterados: ",cursor.rowcount)
conexão.commit()#após alterarmos o banco de dados precisamos chamar o metodo commit se não as alterações serão perdidas