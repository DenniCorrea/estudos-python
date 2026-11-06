## Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
## EX: digite um número: 6.127 O número tem a parte inteira 6
## Utilize a biblioteca "math"

from math import trunc
n = float(input('Insira um número qualquer para ter seu número inteiro: ').replace(',','.'))
# Posso criar uma variavel executando o trunc e depois printar ela
inteiro = trunc(n)
print(f'O número inteiro do número {n} é: {inteiro}')
# Ou executar o trunc dentro do proprio print
print(f'O número inteiro do número {n} é: {trunc(n)}')

## Se eu importar a biblioteca match inteira, fica dessa forma

import math

n = float(input('Insira um número qualquer para ter seu núero inteiro: ').replace(',','.'))
# Posso criar uma variavel executando o math.trunc e depois printar ela
inteiro = math.trunc(n)
print(f'O Número inteiro do número {n} é: {inteiro}')
# Ou executar o math.trunc direto no print
print(f'O Número inteiro do npumero {n} é: {math.trunc(n)}')

#Dessa forma eu crio uma variavel a menos caso nao vá utiliza-lá mais pra frente.
## daria pra usar printando INT, ou :.f1 para limitar a casa decimal, mas o exercicio foi para aprender importar