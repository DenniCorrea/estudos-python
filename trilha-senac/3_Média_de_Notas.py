# Média de Notas
# Faça um programa que calcule a média de um aluno, a partir de três notas informadas pelo usuário.
nome = str(input('Insira o nome do(a) estudante: '))
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
media = (n1 + n2 + n3) / 3
print(f'O(A) estudante {nome} ficou com média {media:.1f}')
