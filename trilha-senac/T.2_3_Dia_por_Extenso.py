'''Dia por Extenso
Implemente um programa que escreva o dia da semana por extenso a 
partir do número do dia, sabendo que a semana começa no Domingo 
como dia zero. Se o número do dia não estiver entre 0 e 6, deve ser 
enviada a mensagem: "Dia da semana inválido'''

input_dia = int(input('Digite o número do dia da semana (0 a 6): '))
if input_dia == 0:
    print('Domingo')
elif input_dia == 1:
    print('Segunda-feira')
elif input_dia == 2:
    print('Terça-feira')
elif input_dia == 3:
    print('Quarta-feira')
elif input_dia == 4:
    print('Quinta-feira')
elif input_dia == 5:
    print('Sexta-feira')
elif input_dia == 6:
    print('Sábado')
else:
    print('Dia da semana inválido')

