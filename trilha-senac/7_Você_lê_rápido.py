# Você lê rápido?
# Faça um programa que calcule o tempo que um livro será lido por uma pessoa a partir do nome do 
# livro, do total de páginas e do tempo em segundos de leitura por página

nome = str(input('Digite seu nome: '))
livro = str(input('Digite o nome do livro: '))
paginas = int(input('Digite o total de páginas do livro: '))
tempo_por_pagina = float(input('Digite o tempo em segundos de leitura por página: '))
tempo_total = paginas * tempo_por_pagina
print(f'{nome}, você finalizará a leitura do livro {livro} em aproximadamente {tempo_total / 3600:.2f} horas.')
