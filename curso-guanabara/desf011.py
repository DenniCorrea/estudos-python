##Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m²

lar = float(input('Digite a largura da parede: ').replace(',','.'))
alt = float(input('Digite a altura da parede: ').replace(',','.'))

m2p = lar*alt
m2t = 2
areap = m2p/m2t
print(f'Você vai precisar de {areap:.1f} latas de tinta que renda 2m²')
print('Você vai precisar de {:.1f} latas de tinta que renda 2m²'.format(areap))
