menu = """
------- BEM-VINDO AO BANCO JGCA -------

Escolha qual operação deseja fazer :

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

  opcao = input(menu)

  if opcao == "1":

    valor = float(input("informe o valor de depósito:"))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito : R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso")
        
    else:

      print('Operação falhou. Digite um valor válido!')

  elif opcao == "2":
    valor = float(input("Informe o valor de saque: "))

    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    print("Saque realizado com sucesso")


    if excedeu_saldo:
       print("Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
      print("Operação falhou! Limite insuficiente!")

    elif excedeu_saques:
        print("Operação Falhou!! Número máximo de saques!")  

    elif valor > 0:
      saldo -= valor
      extrato += f'Saque: R$ {valor:.2f}\n'
      numero_saques += 1
      
    else:

        print("Operação falhou! Valor inválido!")

  elif opcao == "3":

    depositos = saldo

    print("\n========EXTRATO========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo:R$ {saldo:.2f}")
    print("=========================================")  

  elif opcao == "4":
    print("Operação Finalizada com sucesso")
     

    break
    

  else:

    print("Operação Inválida, refaça a operação!")