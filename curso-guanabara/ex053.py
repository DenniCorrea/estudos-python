# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. "apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, a diva em Argel alegra-me a vida".




for c in range(0, 1):
    frase = str(input('Insira uma frase Palímdromo: ').strip())
    palim = str(frase[::-1])
    fraset = frase.replace(' ', '').upper()
    palimt = (fraset[::-1])
    if fraset == palimt:
        print(f'"{frase}" é um Palíndromo, pois escrito ao contrario fica: "{palim}"')
    else:
        print(f'{frase} não é um Palíndromo')





