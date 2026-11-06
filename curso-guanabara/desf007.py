
##Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite sua primeira nota: ').replace(',','.'))
nota2 = float(input('Digite sua segunda nota: ').replace(',','.'))
media = (nota1 + nota2)/2
print(f'A sua média foi de: {media:.1f}')
print('A sua média foi de: {:.3f}'.format(media))