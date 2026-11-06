# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''

'''while sexo != 'M' and sexo != 'F':
    sexo = str(input('Insira seu sexo: \n[ M ] Masculino \n[ F ] Feminino \n...: ').upper()).strip()
    if sexo == 'M' or sexo == 'F':
        sexo = sexo
    if sexo != 'M' and sexo != 'F':
        print(f'Informação inválida, utilize "M" ou "F"')
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Femnino'
print(f'seu sexo é {sexo}')'''

while True:
    sexo = str(input('Insira seu sexo: \n[ M ] Masculino \n[ F ] Feminino \n...: ').upper()).strip()
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            sexo = 'Masculino'
        if sexo == 'F':
            sexo = 'Feminino'
        print(f'Seu Sexo é {sexo}')
        break
    else:
        print('Incorreto, Insira M para Masculino ou F para Feminino')

