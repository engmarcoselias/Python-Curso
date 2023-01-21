# Exercicio 5.10 pagina 47 PDF


'''Programa do exemplo 5.10 editado para executar mesmo se a resposta estiver
com letra maiuscula'''


pontos = 0
questao = 1


while questao <= 3:
     resposta = input('Resposta da questão %d: '% questao)
     if questao == 1 and resposta == 'b' or resposta == 'B':
          pontos = pontos + 1
     if questao == 2 and resposta == 'a' or resposta == 'A':
          pontos += 1
     if questao == 3 and resposta == 'd' or resposta == 'D':
          pontos = pontos + 1
     questao = questao + 1
print('O aluno fes %d Ponto(s)'% pontos)


