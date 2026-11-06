'''Sistema Bancário
Implemente um programa que simule um sistema bancário básico, 
permitindo ao usuário realizar operações em uma conta.
O programa deve apresentar um menu de opções, conforme abaixo:
Menu de Opções
1. Consultar Saldo
2. Realizar Depósito
3. Realizar Saque
0. Sair
Entrada Saída
1 (opcao)
2 (opcao)
100 (deposito)
1 (opcao)
3 (opcao)
20 (saque)
1 (opcao)
0
Saldo atual: R$ 0
Saldo atual: R$ 100
Saldo atual: R$ 80
Cenários de Testes
• O sistema deve iniciar com saldo igual a 0 e 
continuar em execução até que o usuário 
escolha a opção 0.
• Na opção de depósito, o programa deve 
solicitar um valor e adicioná-lo ao saldo.
• Na opção de saque, o programa deve solicitar 
um valor e subtraí-lo do saldo, desde que haja 
saldo suficiente. Caso contrário, deve exibir a 
mensagem “Saldo insuficiente”.
• Caso o usuário informe um valor negativo para depósito ou saque, o 
programa deve exibir a mensagem “Valor inválido” e desconsiderar a 
operação.
• Caso o usuário selecione uma opção inválida no menu, o programa 
deve exibir a mensagem “Opção inválida”.
'''

saldo = 0
saque = 0
deposito = 0

while True:
    movimentacao = int(input('Escolha a opção desejada:\n1. Consaultar Saldo\n2. Realizar Depósito\n3. Realizar Saque\n0. Sair\n'))
    if movimentacao == 0:
        print('! ! ! Transações encerradas ! ! !')
        break    
    elif movimentacao < 0 or movimentacao > 4:
        print('Insira uma opção válida')
        continue
    elif movimentacao == 1: #Saldo
        print(f'Seu saldo atual é de R$ {saldo}')
    elif movimentacao == 2: #Depósito
        deposito = float(input('Insira o valor do deposito: R$ '))
        if movimentacao < 0:
            print('! ! ! Operação inválida ! ! !')
        else:            
            saldo += deposito
            print(f'Seu saldo atual é de R$ {saldo}')
    elif movimentacao == 3: #Saque
        saque = float(input('Insira o valor do saque: R$ '))
        if saque < 0:
            print('! ! ! Operação inválida ! ! !')
        if saldo - saque >= 0:            
            saldo -= saque
            print(f'Seu saldo atual é de R$ {saldo}')
        else:
            print(f'Saldo Insuficiente, seu saldo atual é de R${saldo}')