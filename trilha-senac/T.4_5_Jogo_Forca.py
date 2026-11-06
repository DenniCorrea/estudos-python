print('>>>   BEM VINDO AO JOGO DA FORCA   <<<')

lista_palavra = []
palavra = str(input('Insira a palavra para iniciar o jogo: ').upper())
print('\n' * 50)
lista_palavra.append(palavra)
palavra_separada = list(lista_palavra[0])
lista_letra = ['_'] * len(palavra_separada)
erros = 0
while erros < 7 and '_' in lista_letra:
    print(f'Estado: {" ".join(lista_letra)}')
    letra = str(input('Insira uma letra: ').upper())
    if letra in palavra_separada:
        for i in range(len(palavra_separada)):
            if palavra_separada[i] == letra:
                lista_letra[i] = letra
        if '_' not in lista_letra:
            print(f'Forca: {" ".join(lista_letra)}')
            print(f'Erros: {erros}')
            print('Parabéns! Você descobriu a palavra.')
            break
    else:
        erros += 1
        print(f'Forca: {" ".join(lista_letra)}')
        print(f'Erros: {erros}')