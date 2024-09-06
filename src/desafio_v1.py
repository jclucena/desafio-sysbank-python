menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.upper() == "D":
        deposito = float(input("Qual valor deseja depositar? "))
        if (deposito > 0):
            saldo += deposito
            extrato += f"Deposito efetuado em conta corrente: R$ {deposito:.2f}\n"
            print("\n--> Depósito efetuado com sucesso!")
        else:
            print("\n**Valor inválido. Repita a operação**")

    elif opcao.upper() == "S":
        if (numero_saques <= LIMITE_SAQUES):
            saque = float(input("Qual valor deseja sacar? "))
            if (saque > 0):
                if (saque <= limite):
                    if(saque <= saldo):
                        saldo -= saque
                        extrato += f"Saque efetuado em conta corrente: R$ {saque:.2f}\n"
                        print("\n--> Saque efetuado com sucesso!")
                        numero_saques += 1
                    else:
                        print("\n**Saldo insuficiente.**")
                else:
                    print("\n**Valor solicitado acima do limite máximo por saque!**")
            else:
                print("\n**Valor inválido. Repita a operação**")
        else:  
            print("\n**Limite de Saques diários atingido**")
        
    elif opcao.upper() == "E":
        print("==== Extrato ===")
        if (len(extrato) < 1):
            print("\n **Não foram realizadas movimentacoes.**")
        print(extrato + "\n")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao.upper() == "Q":
        print("SAIR\n")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
