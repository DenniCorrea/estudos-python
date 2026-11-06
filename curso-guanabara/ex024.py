# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Insira o nome da sua Cidade para saber se começa com "SANTO": ').upper().strip().split()
possui = 'SANTO' in cidade[0]

if possui == True:
    print(f'Sua cidade começa com o nome SANTO')
else:
    print(f'Sua cidade NÃO começa com o nome SANTO')
print('Obrigado')
