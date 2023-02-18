#11.13apagando registros

import sqlite3

conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('''delete from agenda where nome="maria"''')
print("Registros apagados : ", cursor.rowcount)
if cursor.rowcount == 1:
    conexão.commit()
    print("Alterações gravadas")
else:
    conexão.rollback()
    print("Alterações abortadas")
conexão.close()