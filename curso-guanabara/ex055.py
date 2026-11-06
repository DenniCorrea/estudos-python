# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.


pesos = []
for c in range(5):
    peso = float(input(f'Insira o {c+1}° peso: '))
    pesos.append(peso)
print(f'O Maior peso da Lista foi {max(pesos)} e o menor foi {min(pesos)}')
