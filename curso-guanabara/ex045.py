# crie um programa que faça o computador jogar jokenpô com você, sendo que o usuário escolhe entre pedra, papel ou tesoura e o computador escolhe aleatoriamente uma dessas opções.
#  O programa deve mostrar o resultado da partida e informar quem venceu.


from random import choice
from time import sleep

print('''
1 - Pedra
2 - Papel
3 - Tesoura''')
escolha = int(input('Escolha a opção desejada: '))
print('JO'), sleep(1), print('KEN'), sleep(1), print('PO!!!!'), sleep(1)
lista = ['Pedra', 'Papel', 'Tesoura']
sorteio = choice(lista)
saida = print(f'O Computador escolheu: {sorteio}')
if (escolha == 1 and sorteio == 'Pedra') or (escolha == 2 and sorteio == 'Papel') or (escolha == 3 and sorteio == 'Tesoura'):
    print('Houve um empate, joga novamente')
elif (escolha == 1 and sorteio == 'Papel') or (escolha == 2 and sorteio == 'Tesoura') or (escolha == 3 and sorteio == 'Pedra'):
    print('Você perdeu ! ! !')
else:
    print('Você Venceu ! ! !')