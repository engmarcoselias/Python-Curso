#11.27trabalhando com datas

import sqlite3

with sqlite3.connect("brasil.db",detect_types=sqlite3.PARSE_DECLTYPES) as conexão:
    conexão.row_factory = sqlite3.Row #row_factory para acessar os campos por nome
    for feriado in conexão.execute("select * from feriados"):
        print("{0} {1}".format(feriado["data"].strftime("%d/%m"),feriado["descrição"]))# para explicação metodo strftime https://www.w3schools.com/python/python_datetime.asp
