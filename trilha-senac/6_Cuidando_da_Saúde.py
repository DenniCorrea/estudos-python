# Cuidando da Saúde
# Faça um programa para calcular o IMC de uma pessoa, a partir de sua altura e peso. A fórmula para 
# calcular o IMC é: peso / altura2

nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso / (altura ** 2)
print(f'{nome}, seu IMC é de {imc:.4f}')
