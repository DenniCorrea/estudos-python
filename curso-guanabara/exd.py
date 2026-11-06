# Crie um programa que leia o número inserido e some os que forem positivos separado dos que forem negativos, 
# ao digitar 0 encerra e mostra a soma dos positivos e negativos

somap = 0 
soman = 0

while True:
    n = int(input('Insira um valor Positivo ou Negativo para soma-los entre si, Digite 0 para Sair: '))
    if n == 0 :
        print('Programa Encerrado ! ! !')
        break
    if n > 0:
        somap += n
    if n < 0:
        soman += n
if somap > 0 and soman < 0:
    print(f'A soma dos números positivos é: {somap}\nA soma dos números negativos é: {soman}')
else:
    print(f'Não houve somatórias ! ! !')
