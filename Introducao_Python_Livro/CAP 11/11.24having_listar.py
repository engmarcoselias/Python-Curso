#11.23utilizando having para listar apenas regiões com mais de 5 estados

'''Diferença de where e having: where e executado antes do agrupamento selecionando os registros que farão parte antes do agrupamento. A clausula having avalia o resultado do agupamento e decide quais farão parte do resultado'''

import sqlite3
print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")
with sqlite3.connect("brasil.db") as conexão:
    for região in conexão.execute("""
            select região, count(*), min(população),
                   max(população), avg(população), sum(população) as tpop
            from estados
            group by região
            having count(*) > 5
            order by tpop desc"""):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*região))