

lista_notas = []
contador = 1
quantidade_aprovado = 0
quantidade_reprovado = 0
while True:
    notas = float(input(f'Insira o valor da {contador}ª Nota:\nPara Sair Digite [ 999 ]').replace(',' , '.'))
    if notas == 999:
        break
    contador += 1
    lista_notas.append(notas)
for nota in lista_notas:
    if nota >= 6:
        quantidade_aprovado +=1
    else:
        quantidade_reprovado +=1

print(f'>> Resultado da Turma <<\nNotas Informadas: {lista_notas}\nMédia da Turma: {sum(lista_notas) / len(lista_notas)}')
print(f'Maior Nota: {max(lista_notas)}\nMenor Nota: {min(lista_notas)}')
print(f'Aprovados: {quantidade_aprovado}\nReprovados: {quantidade_reprovado}')
if quantidade_reprovado != 0:
    print('Situação Geral: Houveram alunos Aprovados!')
else:
    print('Situação Geral: Todos os alunos foram Aprovados!')
    