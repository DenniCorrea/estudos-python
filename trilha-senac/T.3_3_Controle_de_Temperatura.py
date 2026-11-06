'''Controle de Temperatura
Implemente um programa que auxilie no controle de temperaturas 
registradas ao longo do dia em uma cidade. O sistema deve 
permitir que o usuário informe várias temperaturas, uma de cada 
vez, encerrando a entrada quando for digitado o valor 0.
Ao final, o programa deve exibir a maior e a menor temperatura 
registrada.
Caso o usuário informe valores inválidos (por exemplo, 
temperaturas menores que -50°C ou maiores que 60°C), o 
programa deve exibir a mensagem “Temperatura inválida” e 
desconsiderar o valor informado.
Cenários de Testes
Entrada Saída
25
30
18
22
0
Maior temperatura: 30
Menor temperatura: 18
-60
15
40
10
0
Temperatura inválida
Maior temperatura: 40
Menor temperatura: 10
'''

lista_temperatura = []

while True:
    temperatura = float(input('Registre a temperatura\n Caso queira encerrar digite 0: '))
    if temperatura == 0:
        print('Encerrado')
        break
    if (temperatura < -50) or (temperatura > 60):
        print('Temperatura inválida, insira uma temperatura entre -50°C e 60°C')
        continue
    lista_temperatura.append(temperatura)
if lista_temperatura:
    print(f'A Maior temperatura registrada foi {max(lista_temperatura)}\nA Menor temperatura registrada foi {min(lista_temperatura)}')
else:
    print('Nenhuma temperatura foi registrada')


    