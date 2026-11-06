# faça um programa que calcula a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.


somaimpar = 0

for c in range(1, 500+1, 2):
    if c % 3 == 0:
        somaimpar += c
print(f'A soma dos números ímpares múltiplos de 3 é = {somaimpar}')