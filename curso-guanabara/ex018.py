from math import sin, cos, tan, radians
angulo = float(input('Insira um Angulo para saber seu Seno, Cosseno e Tangente: '))
radiano = radians(angulo)
seno = round(sin(radiano))
cosseno = round(cos(radiano))
tangente = round(tan(radiano))
print(f'Seno de °{angulo} é: {seno}')
print(f'Cosseno de °{angulo} é: {cosseno}')
if cosseno == 0:
    tangente = print(f'Não Existe Tangente')
else:
    print(f'tangente de °{angulo} é: {tangente}')
