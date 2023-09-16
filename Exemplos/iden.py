def sacar(valor):

    saldo = 500
    if saldo >= valor:
        print("Saque realizado com sucesso")
        print("Retire as cédulas na boca do caixa!")

    print("Obrigado por ser nosso cliente fiel!")

sacar(300)

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Seu saldo no momento é de: R${float(saldo)}")

depositar(100)