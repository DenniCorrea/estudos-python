'''Fibonacci
Implemente um programa que considerando a sequência de 
Fibonacci, identifique o número de uma posição nessa sequência. 
O usuário deve informar a posição desejada e o programa deve 
apresentar o valor encontrado na posição em questão.
OBSERVAÇÃO
• A sequência de Fibonacci inicia em:
F = { 1, 1, ... } 
• Onde o próximo número é calculado pela soma dos dois últimos: 
F = { 1, 1, 2, 3, 5, 8, 13, 21, 34, ... }
Cenários de Testes
Entrada: 11 -> saída: O valor na posição 10 da sequência de Fibonacci é 55
Entrada: 5 -> saída: O valor na posição 5 da sequência de Fibonacci é 5
Entrada: 1 -> saída: O valor na posição 1 da sequência de Fibonacci é 1
'''

while True:
    n = int(input('Insira a posição desejada na sequência de Fibonacci: '))
    if n <= 0:
        print('Parâmetro inválido')
        continue
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        print(f'O valor na posição {n} da sequência de Fibonacci é {b}.')
        break
