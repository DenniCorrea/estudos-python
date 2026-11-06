'''Semáforo
Implemente um programa que retorne uma mensagem com a ação que 
um pedestre deve realizar ao ver a cor do semáforo. As possíveis ações 
estão listadas abaixo. Se a cor for diferente das opções possíveis, a 
função deve retornar uma mensagem com a informação: "Farol 
inoperante'''

input_cor = str(input('Digite a cor do semáforo: ').strip()).upper() #strip e upper, firula para caso o usuario digite com espacos ou com letras minusculas, (busquei google)
if input_cor == 'VERMELHO':
    print('Espere')
elif input_cor == 'VERDE':
    print('Atravesse')
else:
    print('Farol inoperante')
