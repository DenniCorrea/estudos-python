# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insura a razão: '))
resultado = 0
resultado = termo
for c in range (0, 10):
    print(resultado)
    resultado += razao
print('FIM')
