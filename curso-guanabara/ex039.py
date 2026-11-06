# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print(20*'=',' BEM VINDO AO ALISTAMENTO DO EXÉRCITO ! ! !', 20*'=')
ano = int(input('Para iniciar, insira seu ano de nascimento: '))
data = date.today()
anoatual = data.year
if ano == anoatual - 18:
    print(f'Você está no período de alistamento, aliste-se e não perca o prazo!')
elif ano > anoatual - 18:
    print(f'Você ainda não está no período de alistamento, você deve se alistar em {ano + 18}')
elif ano < anoatual - 18:
    print(f'Você perdeu o prazo, você deveria ter se alistado no ano de {ano + 18}')
    print('SE FUDEU!!!')