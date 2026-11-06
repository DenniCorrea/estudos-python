

quantidade_medicamentos = 0
lista_medicamentos_a = []
lista_medicamentos_b = []
contagem = 1
quantidade_barato_a = 0
quantidade_barato_b = 0
mesmo_preco = 0
quantidade_medicamentos = int(input('Insira a quantidade de medicamentos: '))
for medicamentos in range(quantidade_medicamentos):
    medicamento_a = float(input(f'Insira o {contagem}º Valor do da Farmácia A: R$ '))
    lista_medicamentos_a.append(medicamento_a)
    medicamento_b = float(input(f'Insira o {contagem}º Valor do da Farmácia B: R$ '))
    lista_medicamentos_b.append(medicamento_b)
    contagem += 1
for indice_a in range(len(lista_medicamentos_a)):
        if lista_medicamentos_a[indice_a] < lista_medicamentos_b[indice_a]:
            quantidade_barato_a += 1
        elif lista_medicamentos_a[indice_a] == lista_medicamentos_b[indice_a]:
            mesmo_preco += 1
        else:
            quantidade_barato_b += 1
print(f'FARMAZOOM\nFarmácia A:{lista_medicamentos_a}\nFarmácia B:{lista_medicamentos_b}')
print(f'Produtos mais Baratos:\nNa Farmácia A:{quantidade_barato_a}\nNa Farmácia B: {quantidade_barato_b}\nMesmo Preço: {mesmo_preco}')
print(f'Total\nFarmácia A: R${sum(lista_medicamentos_a)}\nFarmácia B: R${sum(lista_medicamentos_b)}')
print(f'Melhor Opção')
soma_a = sum(lista_medicamentos_a)
soma_b = sum(lista_medicamentos_b)
if soma_a > soma_b:
    print('Farmácia A')
elif soma_a == soma_b:
    print('As duas Farmácias deram o mesmo valor')
else:
    print('Farmácia B')