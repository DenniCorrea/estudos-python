# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
ano = int(input('Insira seu ano de nascimento: '))
dataatual = date.today()
anoatual = dataatual.year

if ano > anoatual:
    print('Insira um ano válido')
elif anoatual - ano <= 9:
    print('MIRIM')
elif anoatual - ano <= 14:
    print('INFANTIL')
elif anoatual - ano <= 19:
    print('JÚNIOR')
elif anoatual - ano <= 20:
    print('SÊNIOR')
elif anoatual - ano > 20:
    print('MASTER')





