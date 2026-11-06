#LAÇO DE REPETIÇÃO FOR
#LAÇO COM VARIAVEL DE CONTROLE NO PYTHON -> LAÇO c NO intervalo(1,10)

"""for c in range(0,5):
    print('Oi')
    print('Fim')
print('Acabou')

for c in range(0,5):
    print(c)

for c in range(5,0,-1):
    print(c)

for c in range(0,10,2):
    print(c)

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite de quanto em quanto: '))
for c in range(i, f+1, p):
    print(c)
print('Obrigado')"""


'''contador = 0
vezes = 10
for c in range(0, 10):
    if vezes == 1:
        print(f'Insira um valor pela última vez:')
    else:
        print(f'Insira um valor {vezes}x')
    n = input('Insira um valor: ')
    vezes -= 1'''


# Insira 5 valores e some eles:

valor = 1
soma = 0
for c in range(0,5):
    if valor == 5:
        v = float(input('Insira o último valor: ').replace(',' , '.'))
    else:
        v = float(input(f'Insira o {valor}° valor: ').replace(',' , '.'))
    soma += v
    valor += 1
if soma == (int(soma)):
    print(f'A soma dos 5 valores é = {soma:.0f}')
else:
    print(f'A soma dos 5 valores é = {soma:.2f}')

# crie uma calculadora que, se inserido um valor positivo soma aos positivos se negativo soma ao negativo





