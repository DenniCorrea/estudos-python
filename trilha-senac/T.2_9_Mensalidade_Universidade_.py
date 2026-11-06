'''Mensalidade Universidade
Implemente um programa que calcule o valor da mensalidade de um 
aluno de faculdade de tecnologia, a partir da sigla do curso, se ele é 
isento (sim ou não) e do desconto em (%) que ele possui. Se a sigla do 
curso não existir conforme tabela abaixo, deve-se apresentar a 
mensagem: “Curso não encontrado”.
Cenários de Testes
Entrada Saída
SI
Não (isento)
0 (desconto)
Valor da mensalidade:
R$ 900.00
ADS
Não (isento)
50 (desconto)
Valor da mensalidade:
R$ 375.00
CS
Sim (isento)
0 (desconto)
Valor da mensalidade:
$ 0.00
INFO
Não (isento)
0 (desconto)
Curso não encontrado
Curso Valor
SI – Sistemas de Informação R$ 900,00
ADS – Análise e Desenvolvimento de Sistemas R$ 750,00
CS – Ciência da Computação R$ 1.150,00
EC – Engenharia da Computação R$ 1.300,00
ES – Engenharia de Software R$ 950,00'''

sigla_curso = input('Digite a sigla do curso: ').upper()
if sigla_curso == 'SI':
    valor_mensalidade = 900.00
elif sigla_curso == 'ADS':
    valor_mensalidade = 750.00
elif sigla_curso == 'CS':
    valor_mensalidade = 1150.00
elif sigla_curso == 'EC':
    valor_mensalidade = 1300.00
elif sigla_curso == 'ES':
    valor_mensalidade = 950.00
else:
    print('Curso não encontrado')
    exit() # Poderia ter usado na calculadora também, mas não usei para não complicar o código. Aqui, como é o final do programa, usei para encerrar a execução. (busquei no google rs)

isento = input('O aluno é isento? (sim/não): ').lower()
if isento == 'sim':
    valor_mensalidade = 0.00
else:
    desconto = float(input('Digite o desconto em (%): '))
    valor_mensalidade = valor_mensalidade - (valor_mensalidade * desconto / 100)

print(f'Valor da mensalidade:\nR$ {valor_mensalidade:.2f}')