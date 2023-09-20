#Tipo de conta
#Em um banco onde se tem dois tipo de contas a normal e a universitaria
#precisamos efetuada o saque no saldo da conta em questão
#sabendo que a conta universitaria não tem direito a cheque especial como a conta normal
import sys

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 1500
cheque = 450

if conta_normal:
    if saque >= saldo:
        print("Saque realizado com sucesso!")
    elif saque > (saldo + cheque):
        print("Saque realizado com sucesso.")
    else:
        print("Não foi possivel realizar o saque. O valor ultrapassa o saldo em conta e cheque especial!")
elif conta_universitaria:
    if saque>= saldo:
        print("Saque efetuado com sucesso!")
                