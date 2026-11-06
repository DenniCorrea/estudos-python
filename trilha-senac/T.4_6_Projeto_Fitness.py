input('>>>   BEM VINDO AO PROJETO FITNESS   <<<\n\nPressione ENTER para continuar...')
dias = int(input('Informe a quantidade de dias monitorados: '))
pesos = []
for i in range(dias):
    peso = int(input(f'Informe o peso do dia {i+1}: '))
    pesos.append(peso)
print(f'Pesos informados: {", ".join(map(str, pesos))}')
maior_peso = max(pesos)
menor_peso = min(pesos)
grafico = ''
for i in range(dias):
    barras = '█' * (pesos[i] // 5)
    grafico += f'Dia {i+1} | {barras} {pesos[i]}\n'
print(grafico)
print(f'Maior peso: {maior_peso} kg (Dia {pesos.index(maior_peso)+1})')
print(f'Menor peso: {menor_peso} kg (Dia {pesos.index(menor_peso)+1})')

