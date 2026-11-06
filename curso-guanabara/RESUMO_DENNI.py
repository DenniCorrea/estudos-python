

#RESUMOS QUE ACHO IMPORTANTE LER ANTES DE PRATICAR PARA RELEMBRAR ALGUNS PONTOS

#LAÇO FOR: O LAÇO FOR QUANDO COMBINADO COM RANGE, ELE VAI FAZER O LOOP NA QUANTIDADE INFORMADA NO RANGE, USADO QUANDO TENHO UM LIMITE QUE CONHEÇO QUE ESSE LAÇO VÁ ACONTECER
lista = [0, 10, 20, 30, 40, 50, 100]
variavel = "Denni"
for c in range(0, 10):
    print(c) #Printando o nome dado ao for no caso "c", vou imprimir o dado lido naquele determinado loop da vez Ex. "0, 1, 2, 3, 4, 5, 6, 7, 8, 9" (No caso ele usa os número do range para printar algo, pois não há outra referêcia)
    print(lista) #Printando a variável "lista" ele vai printar a lista porém usando como referência o range para saber q quantidade que ele deve printar
    print(variavel) #Printando uma variável comum, ele vai printar aquela determinada variável usando como referência o range para saber a quantidade que ele deve printar

#No caso de uma lista onde quero imprimir os dados da lista sem que seja impressa a lista toda de acordo com o range, deve-se abandonar o range e trabalhar em cima da lista:
#QUANDO NÃO TRABALHO COM RANGE, POSSO IMPRIMIR ALGO CITADO NO FOR DAS SEGUINTES MANEIRAS:
lista = [0, 10, 20, 30, 40, 50, 100]
lista[0] = 1 #Aqui eu mudei o valor do índice 0 da lista, que antes era 0, para 1
for l in lista:
    print(l) #Nesse caso como eu tenho uma referência além do range, no caso "lista", ele vai ler os dados da lista e printar 1 a 1 até que ela acabe (ela acabar seria o range da impressão nesse formato)
    print(lista) #Se eu printar "lista" ele vai printar a variável lista completa, por 7 vezes, que é a quantidade de itens dentro da lista, entao seu n° de referencia para printar, vira a quantidade dentro da lista por nao tem range (ERRADO)
                 #Se por algum motivo eu quiser de fato imprimir algo que seja em uma quantidade especifica, preciso usar o print da lista combinado com o range, como feito no exemplo anterior "print(variavel)".

#CASO ESPECIFICO DO USO DO FOR, COM DICIONÁRIO, ONDE EU TENHO UMA CHAVE "KEY" E UM VALOR "VALUES" DESSE DICIONÁRIO, PORTANTO DEVO MENCIONAR O QUE ESTOU QUERENDO PRINTAR NO FOR:
#Printando os valores (values)
dicionario = {'Valor 1': 0, 'Valor 2': 10, 'Valor 3': 20, 'Valor 4': 30, 'Valor 5': 'Denni'}
for valor in dicionario.values(): #Aqui eu menciono que estou querendo printar os valores do dicionario
    print(valor)
#Printando as chaves (keys)
for chave in dicionario.keys(): #Aqui estou mencionando que estou querendo printar as Keys do dicionario
    print(chave)
#Printando os 2, valores e chaves juntos (values, keys)
for dicio in dicionario.items(): #Aqui estou mencionando que estou querendo printar os 2, keys e valores
    print(dicio)

#Exemplo complexo - se eu quiser printar algo com uma condição dentro de uma lista, no caso printar número pares:
numeros = [5, 8 ,2, 9, 0, 1, 3, 4]
for n in numeros:
    if n % 2 != 0:
        continue #Aqui eu digo que se essa a condição do if for verdadeira, ele ignora o restante do laço e começa novamente, lendo o próximo dado
                 #Ou seja, ele lê o número da lista, ele sendo ímpar de acordo com a condição ele volta a ler invés de printar que o número é par
    print(f'O número {n} é par!') #Aqui, caso a condição nao seja verdadeira, ele printa essa mensagem, ou seja, o número que nao for par, ele menciona no print.

#FAÇO WHILE: EXISTEM 2 FORMAS DE CONDICIONAR O WHILE, COMBINADO COM UM IF E LIGANDO "TRUE" E DESLIGANDO ELE "BREAK" USADO QUANDO NAO TENHO IDÉIA DE QUANTAS VEZES SERÁ EXECUTADO
contador = 0
while contador < 10: #Então fazendo if dele, enquanto o contador for menor que 0, continue o looping
    contador += 1 #Aqui eu somo o contador pra nao ficar um looping infinito, o contador chegando em 10 ele para de printar
    print(f'Olá {contador} tananã')
#USANDO TRUE:
contador = 0
while True: #Aqui eu liguei o motor do while
    contador += 1 #Aqui estou manipulado o contador para atingir a condição if que criei abaixo
    if contador > 10: #Aqui coloquei a condição para desligar o while, se contador for maior que 10
        break #aqui dou o comando desligar se a condição for atendida
    print(f'Olá {contador} tananã') #Aqui caso a condição nao seja atendida ele printa essa mensagem

#CONSIDERAÇÕES PARA LISTAS:
#Se eu quiser alterar algo na lista faço:
lista = [0, 10, 20, 30, 40, 50, 100]
lista[0] = 1 #Aqui eu mudei o valor do índice 0 da lista, que antes era 0, para 1
#Se eu quiser incluir algo na lista faço:
lista.append('Denni') #O Valor sempre será inserido após o último índice da lista, ficaria assim -> [0, 10, 20, 30, 40, 50, 100, 'Denni']
#Se eu quiser retirar algo da lista faço:
lista.remove('Denni') #Retiro o valor da lista
#EXISTEM OUTRAS AÇÕES RELACIONADAS A LISTA, SÓ DIGITAR "LISTA." E VAI APARECER AS OPÇÕES
#Se eu quiser puxar a lista relacionada ao índice sem usar dicionário:
for indice, valor in enumerate(lista):
    print(f'Índice:{indice} Valor:{valor}')

    ##               ATENÇÃO             ##
    ##         DIMISTIFICANDO O FOR      ##
    ## É MAIS FÁCIL MANTER O PADRÃO DE SEMPRE CRIAR UM FOR COM RANGE(LEN(LISTA)) E ABAIXO DELE EU TRABALHO COM A CONDIÇÃO COMO SE FOSSE UMA CONDIÇÃO NORMAL, POIS ASSIM EU TENHO UM PADRÃO DE TRABALHO E NÃO FICO CONFUNDINDO COM O FOR SEM RANGE, QUE PODE SER USADO EM OUTRAS SITUAÇÕES, MAS NÃO É O PADRÃO QUE EU USO PARA LISTAS. ##
    
lista_a = [1, 10, 20, 30, 40, 50, 100]
lista_b = [0, 10, 20, 30, 40, 50, 200]
for c in range(len(lista_a)): #Aqui eu estou usando o range para dizer que quero printar a lista de acordo com a quantidade de itens dentro dela, no caso 7, então ele vai printar 7 vezes
    print(c) #aqui eu estou printando o range, então ele vai printar 0, 1, 2, 3, 4, 5, 6, pois ele vai ler a lista de acordo com o range que foi definido acima
    print(lista_a) #Aqui eu estou printando a lista, então ele vai printar a lista completa 7 vezes, pois ele vai ler a lista de acordo com o range que foi definido acima
    print(lista_a[c]) #Aqui eu estou printando a lista de acordo com o range, então ele vai printar 0, 10, 20, 30, 40, 50, 100, pois ele vai ler a lista de acordo com o range que foi definido acima
    #Dessa forma se eu precisar por exemplo comparar 2 listas, eu consigo fazer isso, pois ele vai printar os valores de acordo com o range definido, então consigo comparar os valores de cada lista, pois ele vai printar o valor do índice 0 da lista_a e o valor do índice 0 da lista_b, depois o valor do índice 1 da lista_a e o valor do índice 1 da lista_b e assim por diante.
    print(lista_b[c]) #Aqui eu estou printando a lista_b de acordo com o range, então ele vai printar 0, 10, 20, 30, 40, 50, 200, pois ele vai ler a lista_b de acordo com o range que foi definido acima
    if lista_a[c] > lista_b[c]: #Aqui eu estou comparando os valores das listas de acordo com o range, então ele vai comparar o valor do índice 0 da lista_a com o valor do índice 0 da lista_b, depois o valor do índice 1 da lista_a com o valor do índice 1 da lista_b e assim por diante.
        print(f'O valor da lista_a é maior que o valor da lista_b, sendo {lista_a[c]} > {lista_b[c]}') #Aqui eu estou printando a comparação das listas de acordo com o range, então ele vai printar a comparação do valor do índice 0 da lista_a com o valor do índice 0 da lista_b, depois a comparação do valor do índice 1 da lista_a com o valor do índice 1 da lista_b e assim por diante.