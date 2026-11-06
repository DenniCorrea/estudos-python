# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
numero = int(input('Insira um número inteiro de 0 a 5 e saiba se acertou o número escolhido pelo computador: '))
sorteio = randint (0,5)

if sorteio == numero:
    print(f'O número sorteado pelo computador foi {sorteio}')
    print(f'Parabéns, você acertou o número!')
else:
    print(f'Que pena, você não acertou o número, o número sorteado foi {sorteio}')
print(f'Jogue Novamente !! =)')
