# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade = 0
nome_mais_velho = ''
contagem_mulheres = 0

for c in range(4):
    nome = str(input(f'Insira o nome da {c+1}ª pessoa: ')).strip()
    idade = int(input(f'Insira a idade da {c+1}ª pessoa: '))
    sexo = str(input(f'Insira o sexo da {c+1}ª pessoa, sendo: \n[ M ] - Masculino \n[ F ] - Feminino\n [M / F]: ').upper()).strip()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        maior_idade = idade
        nome_mais_velho = nome
    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        contagem_mulheres += 1
print(f'A média de idade é: {soma_idade / 4}')
print(f'O nome do homem mais velho é: {nome_mais_velho}')
print(f'A quantidade de mulheres menores de 20 anos é igual a: {contagem_mulheres}')