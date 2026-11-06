'''Calculadora com Menu
Implemente um programa que represente uma calculadora. A função deve 
receber dois valores numéricos e o tipo da operação matemática que deve 
realizar nos valores e retornar o resultado do cálculo. As operações 
suportadas estão listadas abaixo, caso seja enviada uma operação 
diferente, deve ser enviada a mensagem: "Operação não suportada".
• O menu pode ser respondido pelo número ou pelo nome da operação.
Cenários de Testes
Entrada Saída
2.0
3.0
Potência
2.0 ^ 3.0 = 8.0
2.0
3.0
3 (Multiplicação)
2.0 * 3.0 = 6.0
9.0
3.0
Divisão
9.0 / 3.0 = 3.0
9.0
3.0
5 (Resto)
9.0 mod 3.0 = 0.0
9.0
3.0
7
Operação não suportada
Menu
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Resto
6. Potência'''

n1 = float(input('Insira o primeiro valor: '))
operacao = str(input('Qual operação matemática deseja fazer?\n' + 10 * '-' + ' DIGITE UMA DAS OPÇÕES ABAIXO ' + 10 * '-' + '\n[ + ] - Soma\n[ - ] - Subtração\n[ * ] - Multiplicação\n[ / ] - Divisão\n[ % ] - Resto\n[ ** ] - Potência\n')).strip()
if operacao not in ['+', '-', '*', '/', '%', '**']:
    print('Digite uma operação válida')
else:
    n2 = float(input('Insira o segundo valor: '))
    if operacao == '+':
        print(f'{n1} {operacao} {n2} = {n1 + n2}')
    if operacao == '-':
        print(f'{n1} {operacao} {n2} = {n1 - n2}')
    if operacao == '*':
        print(f'{n1} {operacao} {n2} = {n1 * n2}')
    if operacao == '/':
        print(f'{n1} {operacao} {n2} = {n1 / n2}')
    if operacao == '%':
        print(f'{n1} {operacao} {n2} = {n1 % n2}')
    if operacao == '**':
        print(f'{n1} {operacao} {n2} = {n1 ** n2}')

        #venho fazendo a impressão no padrão do enunciado, dessa vez usei simbologias diferentes, mas o resultado é o mesmo.
