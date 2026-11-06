## Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
## Calcule o mostre o comprimento da hipotenusa
## Busque um módulo para fazer isso

from math import hypot
co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o catato adjacente: '))
hp = hypot(co,ca)
print(f'Cateto oposto: {co} \nCateto adjacente: {ca} \nA hipotenusa é: {hp}')

# Quando importada a biblioteca completa fica:

import math
co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o catato adjacente: '))
hp = math.hypot(co,ca)
print(f'Cateto oposto: {co} \nCateto adjacente: {ca} \nA hipotenusa é: {hp}')
# Usando o calculo no print
print(f'Cateto oposto: {co} \nCateto adjacente: {ca} \nA hipotenusa é: {math.hypot(co,ca)}')