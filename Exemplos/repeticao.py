import sys
saldo = 1000
opcao = int(input("Selecione a opção desejada.\nOpção [1] Saque\nOpção [2] Extrato\n"))

if opcao == 1:
    print("Opções de notas de R$10 R$20 R$50 R$100")
    saque = float(input("Informe o Valor que deseja sacar: "))
    saldo -= saque
    print(saldo)
elif opcao == 2:
    print(f"O valor em sua conta é de R${saldo}")
else:
    sys.exit("Opção invalida!")