import sys
MAIOR_IDADE = 18
idade = int(input("Qual a sua idade?: "))

if idade >= 18:
    input("Seu cpf para cadastro:")
    input("Digite seu email: ")
    pagamento = int(input("Forma de pagamento da CNH: [1]Débito [2]Crédito [3]Boleto\n"))
    if pagamento == 1:
        print("Certo será débito!")
    elif pagamento == 2:
        print("Certo será crédito!")
    elif pagamento == 3:
        print("Certo sera emitido o boleto e enviado por email.")
    else:
        sys.exit("Opção invalida")
else:
    print("Você não tem a idade necessária para continuar o atendimento. ;-;")