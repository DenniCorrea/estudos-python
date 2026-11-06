

nome_projeto = 'Asilo Lar Jesus'
meta = 1000
lista_doacoes = [0]

print(f'> > > Bem Vindo(a) ao Projeto de Caridade {nome_projeto} < < <')

while True:
    doacao = float(input('DIGITE [ 0 ] PARA SAIR\nInsira o Valor da Doação: R$ '))
    if doacao == 0:
        break
    else:
        lista_doacoes.append(doacao)
if sum(lista_doacoes) >= meta:
    meta = 'Meta Atingida'
else:
    meta = 'Meta não atingida'
print(f'>> Reumo das Doações <<\nProjeto: {nome_projeto}\nDoações Recebidas: {lista_doacoes}')
print(f'\nTotal Arrecadado: R${sum(lista_doacoes)}')
print(f'Maior Doação: R${max(lista_doacoes)}')
print(f'Situação: {meta}')
