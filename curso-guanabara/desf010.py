##Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar (considere US$1,00 = R$3,27)

reais = float(input('Insira quantos reais você tem: R$').replace(',','.'))
dol = reais // 3.27
sobra = reais % 3.27
print(f'Com R${reais}, você consegue comprar U${dol} e, te sobra R${sobra}')