'''Fatorial
Implemente um programa que calcule o fatorial de um número informado 
pelo usuário. Caso o número seja zero, o programa deve informar que o 
parâmetro é inválido.
OBSERVAÇÃO
O fatorial de um número é calculado pela multiplicação desse número 
por todos os seus antecessores até chegar ao número 1.
EXEMPLO
Fatorial de 05: 5 * 4 * 3 * 2 * 1 
Cenários de Testes
Entrada Saída
5 O fatorial de 5 é 120.
0 Parâmetro inválido.
'''


calculo = 0
while True:
    n = int(input('Insira um número para ver seu Fatorial: '))
    if n == 0:
        print('Parâmetro inválido')
        continue
    else:
        calculo = 1
        for c in range(n, 0, -1):
            calculo *= c
        print(f'O fatorial de {n} é {calculo}.')
        break