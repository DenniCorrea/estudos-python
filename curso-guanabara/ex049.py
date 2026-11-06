# Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.



numero = int(input('Insira um número para saber sua tabuada: '))
print(f'A tabuada d0 {numero} é:')
for c in range (1, 10 + 1):
    calc = c * numero
    print(f'{numero} x {c} = {calc}')
    