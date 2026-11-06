# Crie um programa que leia varios numeros inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


soma = 0
maior = 0
menor = 99999999

while True:
    valor = int(input('Insira um valor:'))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor    
    soma += valor
    continuar = str(input('Desenha continuar? Digite:\n[S] - SIM\n[N] - NÂO').upper())
    if continuar == 'N':
        break
    if continuar == 'S':
        continue
print(f'Maior nº digita: {maior}\nMenor nº digita: {menor}\nSoma dos números: {soma}')