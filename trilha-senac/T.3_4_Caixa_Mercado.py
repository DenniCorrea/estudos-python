'''Caixa Mercado
Implemente um programa que simule o funcionamento de um caixa 
de mercado, recebendo do usuário os valores das compras 
realizadas. O programa deve permitir a inserção de múltiplos 
valores, encerrando a entrada quando o usuário informar o valor 0.
Caso o usuário informe valores negativos durante a entrada, o 
programa deve exibir a mensagem “Valor inválido” e 
desconsiderar esse valor no cálculo do total.
Após o cálculo do total, o programa deve solicitar ao usuário em 
quantas vezes deseja parcelar a compra. Caso o usuário informe 
0 ou 1, o programa deve exibir o valor total à vista. Caso informe 
um valor maior que 1, o programa deve exibir o valor total da 
compra e o valor de cada parcela.
Cenários de Testes
Entrada Saída
10
20
30
0
1
Pagamento à vista: R$ 60
15
-5
25
0
3
Valor inválido: -5
Total da compra: R$ 40
Parcelado em 3x de R$ 13.33
'''

compras = []
while True:
    registro_compra = float(input('Registre o valor da compra R$: '))
    if registro_compra == 0:
        break
    elif registro_compra < 0:
        print('Valor inválido, insira um valor válido')
        continue
    compras.append(registro_compra)
if compras:
    soma_compras = sum(compras)
    parcelamento = int(input(f'Sua compra deu um total de R${soma_compras:.2f}\nDeseja parcelar em quantas vezes? ').strip())
    if (parcelamento == 0) or (parcelamento == 1):
        print(f'O valor total ficou de R$ {soma_compras:.2f}')
    elif parcelamento > 1:
        print(f'Total da compra R${soma_compras:.2f}\nParcelado em {parcelamento}x de R${soma_compras / parcelamento:.2f}')
else:
    print('Não houve registro de compras')
