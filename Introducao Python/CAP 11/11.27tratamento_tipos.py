#11.26solicitando o tratamento do tipo dos campos

import sqlite3

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:#detect_types permite que a biblioteca sqlite determine corretamente quais colunas contêm datas e me fornece corretamente um dateobjeto, não uma string quando leio essas colunas.
    for feriado in conexão.execute("select * from feriados"):
        print(feriado)