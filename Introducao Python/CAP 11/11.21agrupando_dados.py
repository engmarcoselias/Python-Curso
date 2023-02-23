#11.20agrupando e contando estados por região

import sqlite3

print("Região Numero de estado")
print("====== =================")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""select região,count(*) from estados group by região"""):#a clausula group by nesse programa e usada para especificar a chave de grupo todos os registros que pertencerem a essa chave são agrupados. A função count(*)retorna quantos registros fazem parte do grupo
        print("{0:6} {1:17}" .format(*região))