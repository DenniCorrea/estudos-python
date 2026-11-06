# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Insira seu salário R$: ').replace(',' , '.'))

if salario > 1250:
    print(f'Seu salário teve 10% de aumento e foi para R${(salario * 0.10) + salario}')
else:
    print(f'Seu salário teve 15% de aumento e foi para R${(salario * 0.15) + salario}')