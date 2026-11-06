#usando f'string ficaria

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
print(f'A soma entre {n1} e {n2} vale {soma}')

#usando .format ficaria

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))