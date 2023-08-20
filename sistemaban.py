saldo = float(0)
limite = 500
LIMIT_SAQUES = 3
NUMERO_SAQUES = 0
extrato=""
menu = f''' 
             //////////////Menu do Banco//////////////

                     [1] SACAR DINHEIRO

                     [2] DEPOSITAR DINHEIRO

                     [3] VERIFICAR EXTRATO

                         [4] SAIR 

             //////////////////////////////////////'''
while True:

    print(menu)
    opcao = int(input("Escolha uma das opções : "))

    if opcao == 1 and NUMERO_SAQUES < LIMIT_SAQUES:
        valor=float(input("Informe a quantia para o saque : "))
        if valor <= 500: 
            if valor <= saldo:
                print("Valor sacado!")
                saldo -= valor
                extrato += f"Saque: R$ {valor}\n"
                print("Valor de saldo atual é : ", saldo)
                NUMERO_SAQUES += 1
                sistema=int(input("Digite qualquer Tecla se quiser continuar com as operações e [0] se deseja sair  :  "))
                if sistema == 0:
                        break
            if valor > saldo :
                print("Saldo insuficiente para operação!")
                print("Valor de saldo atual é : ", saldo)
                sistema=int(input("\nDigite qualquer Tecla se quiser continuar com as operações e [0] se deseja sair  :  "))
                if sistema == 0:
                    break
        elif valor > 500 :
            print("O limite Máximo de Saque atual é R$ 500,00")
            sistema=int(input("\nDigite qualquer Tecla se quiser continuar com as operações e [0] se deseja sair  :  "))
            if sistema == 0:
                 break
        else:
            print("Valor Invalido!!")
    if opcao == 1 and NUMERO_SAQUES == LIMIT_SAQUES:
        print("Limite de Saques diários atingido, \n Tente Novamente Amanhã!!")
        print("quantidade de saques : ",NUMERO_SAQUES )
        sistema=int(input("\nDigite qualquer Tecla se quiser continuar com as operações e [0] se deseja sair  :  "))
        if sistema == 0:
            break
                
    elif opcao == 2 :
        deposito=float(input("Informe o Valor que deseja depositar : ")) 
        saldo +=deposito
        extrato += f"Depósito: R$ {deposito}\n"
        print("Seu novo Saldo É : ", saldo)
        sistema=int(input("\nDigite qualquer Tecla se quiser continuar com as operações e [0] se deseja sair  :  "))
        if sistema == 0:
            break
    elif opcao == 3 :

        print("\n================== Extrato ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo}")
        print("\n===============================================")

        sistema=int(input("\nDigite qualquer Tecla se quiser continuar com as operações e [0] se deseja sair  :  "))
        if sistema == 0:
            break