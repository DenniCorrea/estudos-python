# Escreva um programa que calcule o índice de massa corporal (IMC) de uma pessoa e mostre sua categoria, de acordo com a tabela abaixo:
# - IMC abaixo de 18.5: ABAIXO DO PESO
# - IMC entre 18.5 e 25: PESO IDEAL
# - IMC entre 25 e 30: SOBREPESO
# - IMC entre 30 e 40: OBESIDADE
# - IMC acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Insira seu peso: '))
altura = float(input('Insura sua altura: '))
calc = peso / (altura * altura)

print(calc)

if calc < 18.5:
    print('Você está abaixo do peso!')
elif calc <= 25:
    print('Você está no peso ideal!')
elif calc <= 30:
    print('Você está com sobrepeso!')
elif calc < 40:
    print('Você está obeso(a)!')
elif calc > 40:
    print('Você está com obesidade mórbida!')