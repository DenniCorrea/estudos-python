'''Boletim Aluno
Implemente um programa que informe a classificação de um aluno a 
partir de 3 notas e da quantidade de faltas. O aluno já será considerado 
reprovado se a quantidade de faltas for maior que 04. A tabela ao lado 
apresenta as regras para os intervalos da média. No caso da média 
estar fora de 0 e 10 ou as faltas serem negativas, exibir a mensagem 
“Parâmetros inválidos”'''

input_nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))
input_nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))
input_nota3 = float(input('Digite a terceira nota: ').replace(',', '.'))
input_faltas = int(input('Digite a quantidade de faltas: '))

if input_faltas > 4:
    print(f'Média: {(input_nota1 + input_nota2 + input_nota3) / 3:.1f}.\nSituação: Reprovado por Falta')
else:
    if (input_nota1 + input_nota2 + input_nota3) / 3 >= 8:
        print(f'Média: {(input_nota1 + input_nota2 + input_nota3) / 3:.1f}.\nSituação: Aprovado com sucesso')
    elif (input_nota1 + input_nota2 + input_nota3) / 3 >= 6:
        print(f'Média: {(input_nota1 + input_nota2 + input_nota3) / 3:.1f}.\nSituação: Aprovado')
    else:
        print(f'Média: {(input_nota1 + input_nota2 + input_nota3) / 3:.1f}.\nSituação: Recuperação')

