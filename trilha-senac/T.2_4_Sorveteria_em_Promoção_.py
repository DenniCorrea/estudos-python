'''Sorveteria em Promoção
Implemente um programa que calcule o total a se pagar em uma 
compra na sorveteria, a partir do total de gramas comprado. 
• O preço de 100g é R$ 3,50 mas se o total de gramas for a partir de 
1kg, o preço das 100g diminui 50 centavos. 
• Se o total de gramas for menor ou igual a zero, enviar a mensagem 
“Peso Inválido"'''

input_gramas = float(input('Digite o total de gramas: ').replace(',', '.')) #replace firula caso o usuario use o teclado numero e digite virgula inves de ponto.
if input_gramas <= 0:
    print('Peso inválido')
else:
    if input_gramas >= 1000:
        preco_100g = 3.00
    else:
        preco_100g = 3.50
    total = (input_gramas / 100) * preco_100g
    print(f'O total é R$ {total:.2f}')

