'''Desenhar Retângulo
Implemente um programa que que escreva no terminal a forma de um 
retângulo, a partir do tamanho de sua base e altura, informados pelo 
usuário, conforme exemplo abaixo:
Um retângulo de base 05 e altura 03, resultaria em:
* * * * *
* * * * *
* * * * *
No caso do tamanho ser zero ou menor, a mensagem 
“Retângulo inválido” deve ser exibida.
Cenários de Testes
Entrada Saída
3
3
* * *
* * *
* * *
5
3
* * * * *
* * * * *
* * * * *
0
-2
Retângulo inválido
'''
input_base = int(input('Insira a base do retângulo: '))
input_altura = int(input('Insira a altura do retângulo: '))

if input_base <= 0 or input_altura <= 0:
    print('Retângulo inválido')
else:
    for _ in range(input_altura):
        print('* ' * input_base)
