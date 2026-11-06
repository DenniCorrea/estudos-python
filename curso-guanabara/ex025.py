# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Insira seu nome completo: ').upper().strip()

possui = 'SILVA' in nome

if possui == True:
    print('O seu nome possui SILVA no nome')
else:
    print('O seu nome NÂO possui SILVA no nome')
print('Obrigado')