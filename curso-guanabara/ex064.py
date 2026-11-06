# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).


soma = 0
contador_numeros = 0
while True:
    valor = int(input('Insira os valores para soma, caso queira sair digite "999":\n'))
    if valor == 999:
        break
    else:
        contador_numeros += 1
        soma += valor
print(f'A quantidade de valores digitados foi = {contador_numeros}\nA soma dos valore é igual a {soma}')