##Operadores Aritiméticos##

print('A soma é', 5+2)
print('A subtração é', 5-2)
print('A multiplicação é', 5*2)
print('A divisão é', 5/2)
print('A potência é', 5**2)
print('A divisão inteira é', 5//2)
print('O resto da divisão é', 5%2)

#Ordem de precedência: 
#parenteses ()
#Exponenciação: **
#Multiplicação e divisão: * / // %
#Adição e subtração: + -

#para calcular raiz quadrada de um numero, podemos fazer da seguinte forma:
#raiz quadrada de 81
print('A raiz quadrada de 81 é', 81**(1/2)) #Sempre dividir por 1/2 para raiz quadrada, 1/3 para raiz cubica e assim por diante.
#raiz cubica de 27
print('A raiz cubica de 27 é', 27**(1/3))

#Operadores para strings
#Para concatenar strings, podemos fazer da seguinte forma:
print('Olá, ' + 'Mundo!')
#Para repetir uma string, podemos fazer da seguinte forma:
print('Olá, ' * 5)
#Para repetir uma string e concatenar com outra, podemos fazer da seguinte forma:
print('Olá, ' * 5 + 'Mundo!')

#Ajustes de centralização e alinhamento de strings
#Para centralizar uma string, podemos fazer da seguinte forma:
#eu uso o format e coloco a formatação que quero dentro do {}
#para centralizar utilizo :^20, para direita :>20, para esquerda :<20

nome = input('Qual é o seu nome?')
print('Olá {:^20} seja bem vindo'.format(nome))

#Também posso fazer uma operaçção dentro da formatação:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma entre o número {} e o número {}, \n é igual a {}'.format(n1,n2,n1+n2), end=' =D ')
print('Parabéns')