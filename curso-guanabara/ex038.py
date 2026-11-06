# escreva um programa que leia dois numero inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('Vamos comparar 2 valores? =)')
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print(f'O PRIMEIRO VALOR:{n1} é MAIOR que o SEGUNDO VALOR:{n2}')
elif n1 < n2:
    print(f'O SEGUNDO VALOR:{n2} é MAIOR que o PRIMEIRO VALOR:{n1}')
else:
    print('Os Valores são IGUAIS!!!')
print('Obrigado =)')
