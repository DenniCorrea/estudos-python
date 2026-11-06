# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cedulas = [50, 20, 10, 1]

valor_a_sacar = int(input('Insira o valor a ser sacado: R$'))
print(f'o valor de R${valor_a_sacar} será disponibilizado da seguinte forma:')
for c in cedulas:
    if valor_a_sacar != 0:
        calculo = (valor_a_sacar - c)
    print(f'Células de: {c}')