'''Ingressos para o Cinema
Implemente um programa que calcule o total a se pagar na compra de 
ingressos de cinema, a partir da quantidade de ingressos Inteiras e Meias, 
do dia da semana que será passado o filme e se o filme é nacional. O 
valor do ingresso cheio é R$ 28,50. Considere que:
Cenários de Testes
Entrada Saída
1 (qtd inteiras)
2 (qtd meias)
Quarta-feira (qtd meias)
Sim (nacional)
Total à pagar:
R$ 15.00
0 (qtd inteiras)
2 (qtd meias)
Sábado (qtd meias)
Não (nacional)
Total à pagar:
R$ 28.50
1 (qtd inteiras)
0 (qtd meias)
Quarta-feira (qtd meias)
Não (nacional)
Total à pagar:
R$ 14.50
Regra Valor
Se o dia da semana for quarta-feira, 
o valor do ingresso é único.
R$ 14,50
Se for filme nacional, 
o valor do ingresso é único.
R$ 5,00
• O desconto para filmes nacionais tem prioridade sobre o desconto de 
quarta-feira, ou seja, os dois descontos não podem acontecer ao mesmo 
tempo.'''

quantidade_inteiras = int(input('Digite a quantidade de ingressos inteiros: '))
quantidade_meias = int(input('Digite a quantidade de ingressos meia-entrada: '))
dia_semana = int(input('Digite o dia da semana: 1 - Segunda-feira\n2 - Terça-feira\n3 - Quarta-feira\n4 - Quinta-feira\n5 - Sexta-feira\n6 - Sábado\n7 - Domingo '))
if dia_semana < 1 or dia_semana > 7: #no enunciado não foi pedido para validar o dia da semana, mas achei interessante fazer a validação para evitar que o usuário digite um número inválido.
    print('Dia da semana inválido. Digite um número entre 1 e 7.')
    exit()
filme_nacional = input('O filme é nacional? (sim/não): ').strip().lower()

if filme_nacional == 'sim': #Devo fazer uma validação para o caso do usuário digitar algo diferente de sim ou não, mas como não foi pedido no enunciado, não fiz.
    valor_ingresso = 5.00
elif dia_semana == 3:  # Quarta-feira
    valor_ingresso = 14.50
else:
    valor_ingresso = 28.50

total = (quantidade_inteiras * 28.50) + (quantidade_meias * valor_ingresso)
print(f'Total à pagar:\nR$ {total:.2f}')



