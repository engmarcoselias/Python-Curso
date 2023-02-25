#11.18alterando a tabela

#Em SQL o comando para alterar tabela é (alter table)

'''O comado alter table do SQL lite e limitado temos que alterar um cmapo de cda vez diferente de outros bancos de dados'''

import sqlite3

with sqlite3.connect("brasil.db") as conexão:
    conexão.execute("""alter table estados add sigla text""")
    conexão.execute("""alter table estados add região text""")

