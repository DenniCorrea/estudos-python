# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Insira o valor do produto: '))
print('Escolha a opção de pagamento ')
print('1 - Dinheiro ou Cheque "10% de desconto"')
print('2 - A vista no cartão "5% de desconto"') 
print('3 - Até 2x no cartão') 
print('4 - 3x ou mais no cartão "20% de juros"')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print(f'O valor a ser pago é R$: {preco - (preco * 0.10)}')
elif opcao == 2:
    print(f'O valor a ser pago é R$: {preco - (preco * 0.05)}')
elif opcao == 3:
    print(f'O valor a ser pago é R$: {preco}')
elif opcao == 4:
    print(f'O valor a ser pago é R$: {preco + (preco * 0.20)}')
else:
    print('Selecione uma opção válida')

