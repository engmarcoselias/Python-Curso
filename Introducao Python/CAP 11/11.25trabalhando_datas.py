#11.24criando uma tabela de feriados nacionais

import sqlite3

feriados = [["2018-01-01", "Confraternização Universal"],
            ["2018-04-21", "Tiradentes"],
            ["2018-05-01", "Dia do trabalhador"],
            ["2018-09-07", "Independência"],
            ["2018-10-12", "Padroeira do Brasil"],
            ["2018-11-02", "Finados"],
            ["2018-11-15", "Proclamação da República"],
            ["2018-12-25", "Natal"]]
with sqlite3.connect("brasil.db") as conexão:
    conexão.execute("create table feriados(id integer primary key autoincrement, data date, descrição text)")
    conexão.executemany("insert into feriados(data,descrição) values (?,?)", feriados)