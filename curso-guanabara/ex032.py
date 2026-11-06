# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from calendar import isleap
ano = int(input('Insira o ano passa saber se ele é BISSEXTO: '))
bi = isleap(ano)
if isleap(ano) == True:
    print(f'O ano {ano}, é um ano BISSEXTO')
else:
    print(f'O ano {ano}, NÃO é um ano BISSEXTO')