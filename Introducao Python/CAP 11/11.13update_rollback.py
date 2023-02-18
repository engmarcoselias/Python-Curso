#11.12update com rollback

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("""update agenda set telefone ='2222-2222'""")
print("Registros alterados: ",cursor.rowcount)
if cursor.rowcount == 1:
    conexão.commit()#metodo commit grava as alterações no banco de dados
    print("Alterações Gravadas")
else:
    conexão.rollback()#metodo rollback faz  contrario do commit aborta as alterações deixando o banco de dados como antes
    print("Alterações abortadas")
conexão.close()



