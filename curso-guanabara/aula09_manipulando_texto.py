#FATIAMENTO
#Basicamente é o primeiro número antes do : indica onde vai iniciar, o segundo numero apos o : indica onde vai para e o terceiro numero depois do :
#Indica quais letras serão mostradas sendo puladas por essa quantidade indicada
frase = 'Denni Correa'
print(frase[:12])
print(frase[3:])
print(frase[:12:3])

#len(frase) vai te mostrar quantas espaços estão sendo utilizado dentro da memoria
frase = 'Denni Correa'
print(len(frase))

#frase.count('o') vai contar quantas vezes tem a letra 'o' dentro da frase
frase = 'Denni Correa'
print(frase.count('o'))

#para contar já fazendo o fatiamento podemos usar:
frase = 'Denni Correa'
print(frase.count('o,0,5'))

#frase.find('enn') vai procurar a combinação que voce indicou e ele vai te falar em que posição ela foi encontrada
#se colocado um find inexistente, ele retorna o valor '-1'
frase = 'Denni Correa'
print(frase.find('enn'))

#'Correa' in frase, ele vai te informar com True or False se existe o texto na variavel
frase = 'Denni Correa'
print('Correa' in frase)

#frase.replace('Correa','Fernandes') Substitui
#frase.upper() troca tudo para maiusculo
#frase.lower() troca tudo para minusculo
#frase.capitalize() deixa somente a primeira letra em maiusculo
#frase.title() deixa somente a primeira letra de todas as palavras em maiusculo
#frase.strip() remove qualquer espaço no começo e no final da frase para evitar erros
#frase.rstripe() remove o espaço em branco do lado direito (final) da frase
#frase.lstripe() remove o espaço em branco do lado esquerda (começo) da frase
#frase.split() ele vai dividir a frase nos locais onde tem espaço, separando a str alterando o len por exemplo, criando varias strings em lista
#'-'.join(frase) vai juntar diversas palavras utilizando o '-' para juntar por exemplo.