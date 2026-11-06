# Churrasco de Domingo
# Faça um programa que avalie quanto cada pessoa deve contribuir para o churrasco de domingo. 
# O programa deve receber a quantidade de pessoas e calcular o quanto de carne, linguiça e frango 
# deve ser comprado e quanto cada pessoa deve pagar. Considere que cada pessoa consome 300g 
# de carne (R$ 50,00/kg), 200g de linguiça (R$ 28,00/kg) e 150g de frango (R$ 22,00/kg).

quantidade_pessoas = int(input('Digite a quantidade de pessoas: '))
carne_total = quantidade_pessoas * 0.3
linguiça_total = quantidade_pessoas * 0.2
frango_total = quantidade_pessoas * 0.15
carne_total_preço = carne_total * 50.00
linguiça_total_preço = linguiça_total * 28.00
frango_total_preço = frango_total * 22.00
print(f'Quantidades:\nCarne: {carne_total:.2f} kg', end=' - ')
print(f'Linguiça: {linguiça_total:.2f} kg', end=' - ')
print(f'Frango: {frango_total:.2f} kg')
print(f'\nCusto total:\nCarne: R$ {carne_total_preço:.2f}', end=' - ')
print(f'Linguiça: R$ {linguiça_total_preço:.2f}', end=' - ')
print(f'Frango: R$ {frango_total_preço:.2f}')
print(f'\nCusto total do churrasco: R$ {carne_total_preço + linguiça_total_preço + frango_total_preço:.2f}')
print(f'Cada pessoa deve contriuir com: R$ {(carne_total_preço + linguiça_total_preço + frango_total_preço) / quantidade_pessoas:.2f}')