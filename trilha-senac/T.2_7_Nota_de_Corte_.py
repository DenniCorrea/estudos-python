'''Nota de Corte
Implemente um programa que informe qual a situação de 
um candidato de vestibular a partir da nota que ele tirou, 
da nota de corte e da nota mínima para aprovação. 
Considere as regras abaixo:
Cenários de Testes
Regras de Negócio
Entrada Saída
8.1 (nota candidato)
7.5 (nota de corte)
8.0 (nota mín. aprovação)
Situação candidato: 
Aprovado
6.1 (nota candidato)
7.5 (nota de corte)
8.0 (nota mín. aprovação)
Situação candidato: 
Reprovado
7.7 (nota candidato)
7.5 (nota de corte)
8.0 (nota mín. aprovação)
Situação candidato: 
Lista de Espera
Regra Ação
Nota menor que a nota de corte Reprovado
Nota maior igual a nota mínima de aprovação Aprovado
Nota entre a nota mínima e nota de corte Lista de Espera'''


nota_candidato = float(input('Digite a nota do candidato: ').replace(',', '.'))
nota_corte = float(input('Digite a nota de corte: ').replace(',', '.'))
nota_minima = float(input('Digite a nota mínima para aprovação: ').replace(',', '.'))

if nota_candidato < nota_corte:
    print('Situação candidato:\nReprovado')
elif nota_candidato >= nota_minima:
    print('Situação candidato:\nAprovado')
else:
    print('Situação candidato:\nLista de Espera')
    
