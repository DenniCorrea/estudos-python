# Meta Pessoal
# Faça um programa que calcule em quanto tempo será possível alcançar uma meta pessoal e qual 
# valor deverá ser poupado mensalmente para isso. O usuário deverá informar a descrição da meta, o 
# valor necessário para atingi-la, seu salário mensal e o total das despesas mensais. Considere que, 
# após descontar as despesas, o programa deve reservar automaticamente 30% do valor restante 
# como economia fixa, e que o valor que sobrar após essa reserva poderá ser destinado mensalmente 
# para alcançar a meta.


descricao_meta = input('Digite a descrição da meta pessoal: ')
valor_meta = float(input('Digite o valor necessário para atingir a meta: ').replace(',', '.'))
salario_mensal = float(input('Digite o valor do seu salário mensal: ').replace(',', '.'))
despesas_mensais = float(input('Digite o total das suas despesas mensais: ').replace(',', '.'))
saldo_mensal = salario_mensal - despesas_mensais
reserva_fixa = saldo_mensal * 0.3
valor_disponivel_para_meta = saldo_mensal - reserva_fixa
prazo_estimado_meses = valor_meta / valor_disponivel_para_meta
print(f'Meta: {descricao_meta} ({valor_meta:.2f})\nSalário: R$ {salario_mensal:.2f} - Despesas: R$ {despesas_mensais:.2f}')
print(f'\nSaldo após despesas: R$ {saldo_mensal:.2f}\nReserva fixa (30%): R$ {reserva_fixa:.2f}\nValor disponível para a meta: R$ {valor_disponivel_para_meta:.2f} por mês\nPrazo estimado para atingir a meta: {prazo_estimado_meses:.2f} meses')
