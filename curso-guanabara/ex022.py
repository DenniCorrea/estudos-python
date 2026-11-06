# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O Nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()
print(f'Ajustado com Maiúculas nas primeiras letras: {nome.title()}')
print(f'Transformado para Maiúsculo: {nome.upper()}')
print(f'Trasnformado para Minúsculo: {nome.lower()}')
print(f'O nome completo pessui {len(nome.replace(' ', ''))} letras')
nome2 = nome.split()
print(f'O Primeiro nome possui {len(nome2[0])} letras')
