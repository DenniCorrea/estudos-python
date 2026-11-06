
##Crie um algoritmo que leia um numero e mostre o seu dobro triplo e raiz quadrada
v1 = int(input('Digite um número para descobrir o seu dobro, triplo e raiz quadrada: '))
vdobro = v1*2
vtriplo = v1*3
vrq = v1**(1/2)
print(f'O dobro do {v1} é: {vdobro} \n O triplo de {v1} é: {vtriplo} \n A Raiz quadrada de {v1} é: {vrq:.2f}')
#com .format
print('O dobro do {} é: {} \n O triplo de {} é: {} \n A Raiz quadrada de {} é: {}'.format(v1, vdobro, v1, vtriplo, v1, vrq))