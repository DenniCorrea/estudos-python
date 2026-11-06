'''Tabuada
Implemente um programa que escreva no terminal a tabuada de um 
número informado pelo usuário. 
A mensagem deve estar no formato:
"A x B = X"
Cenários de Testes
Entrada 5 
Saída
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

n = int(input('Insira um número para saber sua tabuada: '))
print(f'A Tabuada do {n} é: ')
for c in range(11):
    print(f'{n} x {c} = {n * c}')
print('Obrigado')
