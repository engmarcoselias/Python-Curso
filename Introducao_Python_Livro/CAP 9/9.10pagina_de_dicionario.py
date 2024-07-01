#geração de pagina web a partir de um dicionario

filmes = {
    "drama":["Cidade kane","O poderoso chefão"],
    "comedia":["Tempos modernos","American Pie","Dr Dolittle"]
}
pagina=open("filmes.html","w",encoding="utf-8")
pagina.write("""
<html lang="pt-BR>
<head>
<meta charset="utf-8>
<title>Filmes</title>
</head>
<body>
""")
for c,v in filmes.items():
    pagina.write("<h1>%s<h1>"% c)
    for e in v:
        pagina.write("<h2>%s</h2"% e)
pagina.write("""
</body>
</html>
""")
pagina.close()

