
##escreve um programa que leia o valor em metros e exiba convertido em centimetros e milimetros

v1 = float(input("Digite o valor em metros: ").replace(",","."))
cent = v1*100
mili = v1*1000
print(f'O valor de {v1} metros, é igual a {cent} centimetros e {mili} em milimetros')
print('O valor de {} metros, é igual a {} centimetros e {} em milimetros'.format(v1,cent,mili))
