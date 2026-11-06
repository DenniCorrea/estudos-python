#Faça um algoritmo que leia o salário de um funcinário e mostre seu novo salário com 15% de aumento.

salr = float(input('Insira seu salário: ').replace(',','.'))

aum = salr * 0.15
salratt = salr + aum

print(f'Seu salário com 15% de aumento fica = R${salratt}')