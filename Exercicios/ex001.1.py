#Tipo de conta
#Em um banco onde se tem dois tipo de contas a normal e a universitaria
#precisamos efetuada o saque no saldo da conta em questão
#sabendo que a conta universitaria não tem direito a cheque especial como a conta normal
import sys

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 500
cheque = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque):
        print("Saque realizado com sucesso.")
    else:
        print("Não foi possivel realizar o saque. O valor ultrapassa o saldo em conta e cheque especial!")
elif conta_universitaria:
    status = "Sucesso" if saque <= saldo else "Falha"
    print(f"{status} ao executar o saque")
else:
    sys.exit("Não foi possivel reconhecer o tipo de conta.")