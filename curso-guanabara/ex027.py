# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input('Insira seu nome completo: ').strip().title()
nome2 = nome.split()

print(f'Primeiro Nome: {nome2[0]}')
print(f'Último Nome: {nome2[2]}')

# Na resolução do exercicio pra conseguir fazer independente do tamanho do nome ele fez da seguinte forma:


nome = input('Insira seu nome completo: ').strip().title()
nome2 = nome.split()

print(f'Primeiro Nome: {nome2[0]}')
print(f'Último Nome: {nome2[len(nome2)-1]}')