# Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Insira um número inteiro: '))
print('\n', 20*'=', f'Converta seu número', 20*'=')
print(f'\n1 - Conversão BINÁRIA\n2 - Conversão OCTAL\n3 - Conversão HEXADECIMAL')
conversao = int(input('Digite o número para opção desejada: '))
if conversao == 1:
    print(f'O número {numero} convertido para BINÁRIO é: {bin(numero)[2:]}')
elif conversao == 2:
    print(f'O número {numero} convertido para OCTAL é: {oct(numero)[2:]}')
elif conversao == 3:
    print(f'O número {numero} convertido para HEXADECIMAL é: {hex(numero)[2:]}')
else:
    print('Selecione uma das opções acima: 1, 2 ou 3')
print('Obrigado volte sempre!')
