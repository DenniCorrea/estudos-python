

faturamento_mensais = []
contador = 1
subiu = False
desceu = False
constante = False
sem_padrao = False
quantidade_meses = int(input('Insira a quantidade de meses que deseja analisar: '))
for lista in range(quantidade_meses):
    faturamentos = float(input(f'Insira o {contador}º Faturamento: R$ '))
    contador += 1
    faturamento_mensais.append(faturamentos)
    analise_calculo = faturamento_mensais[0]
for analise in faturamento_mensais[1:]:
    if analise > analise_calculo:
        subiu = True
    elif analise < analise_calculo:
        desceu = True
    elif analise == analise_calculo:
        constante = True
    else:
        sem_padrao = True
    analise_calculo = analise
if subiu and not desceu and not constante:
    print('Situação: CRESCENTE')
elif desceu and not subiu:
    print('Situação: QUEDA')
elif constante and not subiu or not desceu:
    print('Situação: CONSTANTE')
else:
    print('Situação: SEM PADRÃO')