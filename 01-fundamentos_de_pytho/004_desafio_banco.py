"""Fomos contratados por um grande bancopara desenvolver o seu novo sistema. Essebanco deseja modernizar suas operações epara isso escolheu a linguagem Python.Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito,saque e extrato."""

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor que deseja depositar: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Valor depositado: R${valor:.2f}\n"
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Valor inserido invalido!")
            
    elif opcao == 2:
        valor = float(input("Digite o valor que deseja sacar: R$"))

        if numero_saques >= LIMITE_SAQUES:
            print("Voce excedeu o numero de saque diario")
        elif valor > 500 or valor < 0:
            print("Valor invalido. O Valor de saque deve ser entre R$1 até R$500")
        elif valor > saldo:
            print("O valor maior que o saldo atual")
        else:
            numero_saques += 1
            saldo -= valor
            extrato += f"Valor retidado: R${valor:.2f}\n"
            print(f"Valor sacado com sucesso, o seu saldo atual eh: R${saldo:.2f}")

    elif opcao == 3:
        print("#"*50)
        print(f"EXTRATO".center(50)) #a função .center(), centraliza ums string ou variavel em um print.
        print("#"*50)
        print("Sem extrato" if not extrato else extrato) #verificação se o extrato contém algum processo como deposito ou saque
        print(f"Saldo atual: R${saldo:.2f}".center(50)) 
        print("#"*50)

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")