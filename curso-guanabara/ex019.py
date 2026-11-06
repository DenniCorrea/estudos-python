## Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
## Lendo o nome deles e escrevendo o nome escolhido
## Utilizando modulo também

from random import choice
nome1 = input('Digite o nome do primeiro Aluno: ')
nome2 = input('Digite o nome do segundo Aluno: ')
nome3 = input('Digite o nome do terceiro Aluno: ')
nome4 = input('Digite o nome do quarto Aluno: ')
nome5 = input('Digite o nome do quinto Aluno: ')
input('Pressione enter para sortear quem irá apagar o quadro')
lista = [nome1, nome2, nome3, nome4, nome5]
sorteio = choice(lista)
print(f'{sorteio}')