'''Desafio da Soletração
Implemente um programa que simule um treinamento de soletração
utilizado em uma competição escolar. O sistema deve solicitar ao usuário 
que digite uma palavra e, em seguida, pedir que ele informe essa 
mesma palavra letra por letra.
A cada letra digitada, o programa deve concatená-la para formar uma 
nova palavra. O processo deve continuar até que o usuário digite o 
caractere “0”, indicando o fim da soletração.
Ao final, o programa deve exibir:
• A palavra original digitada;
• A palavra formada a partir das letras informadas.
Cenários de Testes
Entrada Saída
casa
c
a
s
a
0
Palavra original: casa
Palavra soletrada: casa
sol
s
o
l
0
Palavra original: sol
Palavra soletrada: sol
lua
l
a
0
Palavra original: lua
Palavra soletrada: la
'''

lista_soletracao = []
contador_letra = 1
soletracao = 1
palavra = 1
while True:
    if soletracao == '0': #Precisei inserir esse break no retorno do break do if do 2º While, para ele nao contar o '0' na lista_soletracao
        break
    palavra = str(input('Para Sair Digite 0\nDigite uma palavra: '))
    if palavra == '0':
        break
    while soletracao != '0': #2º While
        soletracao = str(input(f'Soletre:\nDigite a {contador_letra}ª letra: \n! ! ! Digite 0 quando terminar ! ! !\n'))
        contador_letra += 1
        if soletracao == '0':
            break
        lista_soletracao.append(soletracao)
if lista_soletracao:
    resultado = ''.join(lista_soletracao)
    print(f'Palavra original: {palavra}\nPalavra soletrada: {resultado}')
else:
    print('Encerrado !\nNão houve uma palavra digitada')





