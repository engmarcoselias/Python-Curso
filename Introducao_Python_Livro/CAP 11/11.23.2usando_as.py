#11.22funções de agregação com order by

import sqlite3
print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
            select região, count(*), min(população),
                   max(população), avg(população), sum(população) as tpop
            from estados
            group by região
            order by tpop desc"""):#usando (as)para dar nome a coluna soma=(sum(população)) e alterando no order by
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))
    print("\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
        *conexão.execute("""
            select count(*), min(população), max(população),
                   avg(população), sum(população) from estados""").fetchone()))