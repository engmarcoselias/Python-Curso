#11.17consulta dos estados brasileiros ordenados por nome

import sqlite3

conexão = sqlite3.connect("brasil.db")
conexão.row_factory = sqlite3.Row
print("%3s %-20s %12s"% ("id","Estado","População"))
print("="*37)
for estado in conexão.execute("select * from estados order by população desc"):#por padrão a clausa (order by) mostra por ordem crescente mas adicionando desc sera mostrado por ordem decrescente
    print("%3d %-20s %12d"%(estado["id"],estado["nome"], estado["população"]))
conexão.close()