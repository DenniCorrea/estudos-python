
#Desafio: Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número para saber seu successor e seu antecessor: '))
sus = n1+1
ant = n1-1
print(f'O sucessor do número {n1}, é o número {sus} \n e o antecessor dele é o {ant}', end=" ---> ")
print(f'Parabéns!')
#com .format
print('o Sucessor do número {}, é o número {} \n e o antecessor dele é o {}'.format(n1,sus,ant), end=" --->> ")
print('Parabeeens!')