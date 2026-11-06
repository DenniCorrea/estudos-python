# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# Cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Para calcular sua pasasgem, insira quantos KM é sua trajetória: '))
if distancia <= 200:
    print(f'Sua viagem vai custar R${distancia * 0.50:.2f}')
else:
    print(f'Sua viagem vai custar R${distancia * 0.45:.2f}')

distancia = float(input('Para calcular sua pasasgem, insira quantos KM é sua trajetória: '))
dista = distancia * 0.50
distb = distancia * 0.45
if distancia <= 200:
    print(f'Sua viagem vai custar R${dista:.2f}')
else:
    print(f'Sua viagem vai custar R${distb:.2f}')