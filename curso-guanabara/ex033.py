# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print(f'Olá, para descobrir qual o maior e qual o menor número dos 3 digitados')
n1 = float(input('Insira o 1° Número: '))
n2 = float(input('Insira o 2° Número: '))
n3 = float(input('Insira o 3° Número: '))

lista = [n1, n2, n3]
maiornumero = max(lista)
menornumero = min(lista)

print(f'O Maior número dentre {lista} é {maiornumero} \n O Menor número dentre {lista} é {menornumero}')