# Açaiteria
# Faça um programa para calcular o total de uma venda de açaí a partir das quantidades compradas 
# para cada tamanho: pequeno, médio e grande, sabendo que o valor do açaí é R$ 13,50, R$ 15,00 e 
# R$ 17,50 respectivamente. O programa também deve receber o valor do cupom de desconto em 
# porcentagem.

pequeno = int(input('Digite a quantidade vendida de açaí pequeno: '))
médio = int(input('Digite a quantidade vendida de açaí médio: '))
grande = int(input('Digite a quantidade vendida de açaí grande: '))
cupom_desconto = float(input('Digite o valor do cupom de desconto em porcentagem: ').replace('%', ''))
valor_total = (pequeno * 13.50) + (médio * 15.00) + (grande * 17.50)
desconto = valor_total * (cupom_desconto / 100)
print(f'Seu pedido foi registrado.\n- Açai P: {pequeno}\n- Açai M: {médio}\n- Açai G: {grande}')
print(f'\nDesconto de {cupom_desconto:.0f}% aplicado.\nTotal: R$ {valor_total - desconto:.2f}')
