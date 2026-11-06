'''Desenhar Triângulo
Implemente um programa que que escreva no terminal a forma de um 
triângulo, a partir do tamanho de sua altura, informado pelo usuário, 
conforme exemplo abaixo:
Um triângulo de altura 05, resultaria em:
*
* *
* * *
* * * *
* * * * *
No caso do tamanho ser zero ou menor, a mensagem 
“Triângulo inválido” deve ser exibida.
Cenários de Testes
Entrada Saída
2 *
* *
3 *
* *
* * *
0 Triângulo inválido'''

input_altura = int(input('Insira a altura do triângulo: '))
if input_altura <= 0:
    print('Triângulo inválido')
else:
    for i in range(1, input_altura + 1):
        print('* ' * i)