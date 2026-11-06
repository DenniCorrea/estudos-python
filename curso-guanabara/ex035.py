# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

retaa = float(input('Insira o tamanho da 1° Reta: '))
retab = float(input('Insira o tamanho da 2° Reta: '))
retac = float(input('Insira o tamanho da 3° Reta: '))

if (retaa + retab > retac) and (retab + retac > retab) and (retab + retac > retaa):
    print(f'Com essas medidas de {retaa}, {retab} e {retac}, é possivel fazer um triangulo!')
else:
    print(f'Com essas medidas de {retaa}, {retab} e {retac}, NÃO é possivel fazer um triangulo!')
    