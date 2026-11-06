#Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Insira um número inteiro para saber se ele é PAR ou ÍMPAR: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')