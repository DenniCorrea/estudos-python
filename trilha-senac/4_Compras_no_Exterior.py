# Compra no Exterior
# Faça um programa para simular a conversão de um valor em real para dólar. Considere a cotação do 
# dólar em R$ 5,42.

valor_real = float(input('Digite o valor em reais: '))
cotação_dólar = 5.42
valor_dólar = valor_real / cotação_dólar
print(f'Valor em real R$ {valor_real:.2f}.')
print(f'Valor em dólar $ {valor_dólar:.2f}.')

