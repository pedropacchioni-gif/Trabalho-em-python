saldo = 0
extrato = []


def depositar(saldo, extrato):
    valor = float(input("Digite o valor do depósito: R$ "))

    if valor > 0:
        saldo = saldo + valor
        extrato.append("Depósito: R$ " + str(valor))
        print("Depósito realizado com sucesso!")
        print("Saldo atual: R$", saldo)
    else:
        print("Valor inválido.")

    return saldo, extrato


def sacar(saldo, extrato):
    valor = float(input("Digite o valor do saque: R$ "))

    if valor > 0:
        if valor <= saldo:
            saldo = saldo - valor
            extrato.append("Saque: R$ " + str(valor))
            print("Saque realizado com sucesso!")
            print("Saldo atual: R$", saldo)
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor inválido.")

    return saldo, extrato


def mostrarExtrato(saldo, extrato):
    print("===== EXTRATO =====")

    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)

    print("Saldo atual: R$", saldo)


opcao = None

while opcao != "4":
    print()
    print("===== MENU =====")
    print("1 - Adicionar Dinheiro")
    print("2 - Sacar Dinheiro")
    print("3 - Mostrar Extrato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "2":
        saldo, extrato = sacar(saldo, extrato)

    elif opcao == "3":
        mostrarExtrato(saldo, extrato)

    elif opcao != "4":
        print("Opção inválida.")

print("Sistema encerrado.") 
