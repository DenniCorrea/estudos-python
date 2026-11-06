# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date
data = date.today()
ano = data.year
mai = 0
mei = 0
contagem = 1
for c in range(0, 7):
    datan = int(input(f'Insira o {contagem}° ano de seu nascimento: '))
    contagem += 1
    if (ano - datan) >= 18:
        mai += 1
    else:
        mei += 1
print(f'Das 7 pessoas inseridas, {mai} são maiores de idade e, {mei} são menores de idade')
print('FIM')



