# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Exemplo: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = (input('Insira um número inteiro de 0 a 9999: ')).strip()
print(f'Unidade: {numero[3:]}')
print(f'Dezena: {numero[2:3]}')
print(f'Centena: {numero[1:2]}')
print(f'Milhar: {numero[0:1]}')

#Outra forma de fazer de acordo com o Guanabara na correção seria transformar o numero em string pra mostrar a letra da string

numero = int(input('Insira um número inteiro: '))
n = str(numero)

print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

#Outro jeito que ensiou e que nao nos limita a quantidade exatava de casas decimais é:

numero = int(input('Insira um número inteiro: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
dm = numero // 10000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
print(f'Dezena de Milhar: {dm}')