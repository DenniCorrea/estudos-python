nome = input('Digite seu nome: ')
print('É um prazer te conhecer {}!'.format(nome))

## após ter tirado duvidas com o Claude a respeito do Print, em exercicios elaboramos a seguinte situação:

nome = input('Qual é o seu nome?') 
idade = input(f'Qual é a sua idade {nome}') 
cidade = input(f'{nome} em que cidade você mora?')
print(f'{nome}, você tem {idade} anos e ainda está aprendendo, na cidade de {cidade}')