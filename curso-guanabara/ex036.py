# Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

vlcasa = float(input('Insira o Valor da Casa: '))
salario = float(input('Insira seu salário: '))
anos = float(input('Insira em quantos anos vai financiar: '))

limite = salario * 0.30
prestacao = vlcasa / (anos * 12)

if prestacao > limite:
    print(f'Empréstimo REPROVADO, a prestação mensal excedeu 30% do seu salário')
else: 
    print(f'Empréstimo APROVADO, prestação mensal de R${prestacao:.2f}')