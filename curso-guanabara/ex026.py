# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').strip().lower()
print(f'A frase {frase} contém {frase.count('a')} letras "A"')
print(f'A primeira letra "A" aparece na posição {frase.find('a')}')
print(f'A última letra "A" aparece na posição {frase.rfind('a')}')