# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Insira a velocidade do carro: ').replace(',' , '.'))
if velocidade > 80:
    calcmulta = (velocidade - 80) * 7
    print(f'Sua velicidade foi de {calcmulta}km/h \n você terá que pagar R${calcmulta:.2f} de multa')
else:
    print(f'Você passou dentro do limite de velocidade!')
print(f'Até a próxima')