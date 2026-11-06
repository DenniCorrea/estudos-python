#Escreve um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
# e R$0,15 por KM rodado.

km = float(input('Insira quantos KM você rodou: '))
dia = float(input('Insira quantos dias esse carro ficou alugado: '))

calcdia = dia * 60
calckm = 0.15 * km

print(f'O valor a ser pago por esse aluguel é de: R${calcdia + calckm:.2f}')
