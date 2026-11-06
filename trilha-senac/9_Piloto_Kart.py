# Piloto Kart
# Faça um programa que avalie a performance de um piloto, a partir do tamanho da pista em metros, 
# da quantidade de voltas e do tempo total em segundos que ele completou a primeira volta. O 
# programa deve calcular a distância total da corrida em quilômetros e a previsão de tempo em 
# minutos que ele concluirá a corrida se manter seu tempo de volta.

tamanho_pista = float(input('Digite o tamanho da pista em metros: ').replace(',', '.'))
quantidade_voltas = int(input('Digite a quantidade de voltas: '))
tempo_primeira_volta = float(input('Digite o tempo total em segundos que ele completou a primeira volta: ').replace(',', '.'))
print(f'Análise Preditiva Concluída\n--\nDistância total a ser percorrida: {(tamanho_pista * quantidade_voltas) / 1000:.2f} km.\nPrevisão de conclusão: {tempo_primeira_volta * quantidade_voltas / 60:.1f} minutos.')
