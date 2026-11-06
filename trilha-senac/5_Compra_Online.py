# Compra Online
# Faça um programa para calcular o valor final de uma compra, a partir do valor da compra e do 
# cupom de desconto. O cupom diz a porcentagem do desconto.

nome = str(input('Digite seu nome: '))
valor_compra = float(input('Digite o valor da compra: '))
cupom_desconto = float(input('Digite o valor do cupom de desconto em porcentagem: ').replace('%', ''))
desconto = valor_compra * (cupom_desconto / 100)
valor_final = valor_compra - desconto
print(f'Olá {nome}, sua compra de R$ {valor_compra:.2f} foi confirmada!')
print(f'Foi aplicado um desconto de {cupom_desconto:.2f}%.')
print(f'O total final ficou em R$ {valor_final:.2f}')
