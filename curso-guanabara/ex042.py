# Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 
# Se forem capazes de formar um triângulo, informe também qual tipo de triângulo será formado: Equilátero, Isósceles ou Escaleno.

retaa = float(input('Insira o tamanho da 1° Reta: '))
retab = float(input('Insira o tamanho da 2° Reta: '))
retac = float(input('Insira o tamanho da 3° Reta: '))


if retaa + retab <= retac or retaa + retac <= retab or retab + retac <= retaa:
    print(f'Com essas medidas de {retaa}, {retab} e {retac}, NÃO é possivel fazer um triangulo!')
elif retaa == retab == retac:
    print(f'esse triângulo será EQUILÁTERO')
elif retaa == retab != retac or retaa == retac != retab or retab == retac != retaa:
    print(f'esse triângulo será ISÓSCELES')
elif retaa != retab and retab != retac and retaa != retac:
    print(f'esse triângulo será ESCALENO')

