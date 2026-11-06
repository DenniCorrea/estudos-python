#coletar dados sobre o input (qual tipo primitivo), se é maiusculo, se é numero, str e etc.
#antes um exemplo: i type te trás o tipo mencionado no input, se falei ser str ele informa ser str, se falei ser float ele indicará float (indica a conversão)
v1 = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(v1))

#agora com uma forma que ele lê o que foi imputado e me da o valor do realmente foi digitado pelo usuario no input

v1 = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(v1))
#uma pergunta relacionada ao .is
print('só tem espaços?', v1.isspace())
#uma pergunta relacionada ao .is
print('é decimal?', v1.isdecimal())
#uma pergunta relacionada ao .is
print('está tudo em minúsculo?', v1.islower())

#isso chama Dissecar uma variavel, ou seja, pegar cada caracter e analisar ele separadamente