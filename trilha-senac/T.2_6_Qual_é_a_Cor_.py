'''Qual é a cor?
Implemente um programa que informe a cor resultante a partir de 
duas cores primárias. Se as cores informadas não forem primárias, 
a função deve informar uma mensagem dizendo que apenas cores 
primárias são aceitas.
Cenários de Testes
Entrada Saída
Vermelho
Azul
A combinação resulta em: 
Roxo
Azul
Vermelho
A combinação resulta em: 
Roxo
Vermelho
Rosa
Apenas cores primárias são 
aceitas.
Rosa
Vermelho
Apenas cores primárias são 
aceitas.'''

input_cor1 = input('Digite a primeira cor: ').upper()
input_cor2 = input('Digite a segunda cor: ').upper()

if input_cor1 in ['VERMELHO', 'AZUL', 'AMARELO'] and input_cor2 in ['VERMELHO', 'AZUL', 'AMARELO']:
    if input_cor1 == input_cor2:
        print(f'As cores {input_cor1} e {input_cor2} resultam em: {input_cor1}')
    else:
        print(f'As cores {input_cor1} e {input_cor2} resultam em: {input_cor1 + input_cor2}')
else:
    print('Apenas cores primárias são aceitas.')