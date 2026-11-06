# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contagem = 1

print(5 * '=-', 'Vamos somar somente os números pares', 5 * '-=')
for c in range (0, 5):
    n = int(input(f'Insira o {contagem}° Número: '))
    contagem += 1
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares é = {soma}\n', 13 * '=-', 'FIM', 13 * '-=')

