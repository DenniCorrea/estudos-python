'''Orçamento Familiar
Implemente um programa que informe a situação de um orçamento 
familiar baseado no total de ganhos e gastos. Se o total de ganhos 
for maior ou igual ao total de gastos, deve ser exibida a mensagem: 
"Você está dentro do orçamento!", senão "Você está fora do 
orçamento! Não gaste mais!'''


input_ganhos = float(input('Digite o total de ganhos: '))
input_gastos = float(input('Digite o total de gastos: '))

if input_ganhos >= input_gastos:
    print('Você está dentro do\norçamento!')
else:
    print('Você está fora do orçamento!\nNão gaste mais!')