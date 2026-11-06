depositos = []
saques = []
cancelamentos = []
transacao = input("Digite o valor da transação (ou -1 para encerrar): ")
while transacao != "-1":
    if transacao == "0":
        if depositos or saques:
            if cancelamentos:
                ultima_transacao = cancelamentos.pop()
                if ultima_transacao > 0:
                    depositos.remove(ultima_transacao)
                else:
                    saques.remove(ultima_transacao)
            else:
                if depositos:
                    ultima_transacao = depositos.pop()
                elif saques:
                    ultima_transacao = saques.pop()
                cancelamentos.append(ultima_transacao)
        else:
            print("Não há transações para cancelar.")
    else:
        valor = float(transacao)
        if valor > 0:
            depositos.append(valor)
        elif valor < 0:
            saques.append(valor)
    transacao = input("Digite o valor da transação (ou -1 para encerrar): ")
print("Saldo final:", sum(depositos) + sum(saques))
