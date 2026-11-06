##Faça um algotimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

pdt = float(input('Insira o preço do produto: ').replace(',','.'))

desc = pdt * 0.05
pdtatt = pdt - desc

print(f'O produto com 5% de desconto fica = a R${pdtatt:.2f}')