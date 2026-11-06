## O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
## Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import sample
nome1 = input('Digite o nome do primeiro Aluno: ')
nome2 = input('Digite o nome do segundo Aluno: ')
nome3 = input('Digite o nome do terceiro Aluno: ')
nome4 = input('Digite o nome do quarto Aluno: ')
nome5 = input('Digite o nome do quinto Aluno: ')
input('Pressione enter para sortear quem irá apagar o quadro')
lista = [nome1, nome2, nome3, nome4, nome5]
sorteio = sample(lista, 5)
print(f'{sorteio}')