'''Calculadora
Implemente um programa que simule uma calculadora simples, permitindo 
ao usuário escolher entre as quatro operações básicas: adição, subtração, 
multiplicação e divisão.
Menu de Opções
1. Somar
2. Subtrair
3. Multiplicar
4. Dividir
0. Sair
Entrada Saída
1 (opcao)
10 (n1)
5 (n2)
2 (opcao)
8 (n1)
5 (n2)
3 (opcao)
4 (n1)
3 (n2)
4 (opcao)
5 (n1)
2 (n2)
0
Resultado: 10 + 5 = 15
Resultado: 8 - 5 = 3
Resultado: 4 * 3 = 12
Resultado: 5 / 2 = 2.5
Fim.
Cenários de Testes
O programa deve apresentar um menu de opções, 
conforme ao lado: 
Enquanto o usuário não escolher a opção 0, o 
programa deve continuar em execução. Para cada 
operação selecionada (de 1 a 4), o sistema deve 
solicitar dois valores numéricos, realizar o cálculo 
correspondente e exibir o resultado.
Caso o usuário selecione uma opção inválida, o programa deve exibir a 
mensagem “Opção inválida”. Além disso, na operação de divisão, o 
programa deve verificar se o divisor é igual a zero e, nesse caso, exibir a 
mensagem “Divisão por zero não permitida”'''


while True:
    operacao = int(input('Escolha qual operação deseja fazer, digite:\n1. Somar\n2. Subtrair\n3. Multiplicar\n4. Dividir\n0 .Sair\n'))    
    if operacao < 0 or operacao > 4:
          print('! ! ! Operação inválida ! ! !')          
    elif operacao == 0:
        print('Fim.')
        break
    elif operacao == 1:
        n1 = float(input('Insira o 1º valor para operação: '))
        n2 = float(input('Insira o 2º valor para operação: '))
        print(f'Resultado: {n1} + {n2} = {n1 + n2}')
    elif operacao == 2:
        n1 = float(input('Insira o 1º valor para operação: '))
        n2 = float(input('Insira o 2º valor para operação: '))
        print(f'Resultado: {n1} - {n2} = {n1 - n2}')
    elif operacao == 3:
            n1 = float(input('Insira o 1º valor para operação: '))
            n2 = float(input('Insira o 2º valor para operação: '))
            print(f'Resultado: {n1} * {n2} = {n1 * n2}')
    elif operacao == 4:
                n1 = float(input('Insira o 1º valor para operação: '))
                n2 = float(input('Insira o 2º valor para operação: '))
                while n2 == 0:
                    print('Divisão por 0 não permitida, insira o valor novamente: ')
                    n2 = float(input('Insira o 2º valor para operação: '))
                print(f'Resultado: {n1} / {n2} = {n1 / n2}')

                #Achei o código muito grande, fui pesquisar no google a refatoração dele e vi que, eu poderia ter feito o n1 e n1
                #por fora dos elif, pedindo uma vez só, mas não tive esse discernimento, vou tentar nas próximas.





