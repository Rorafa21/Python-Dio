cadastro = []
register = True

while register == True:
    
    nome = input("Qual seu nome?: ")
    cpf = int(input("Qual seu cpf?: "))
    idade = int(input("Qual sua idade?: "))

    cadastro.append(nome)
    cadastro.append(cpf)
    cadastro.append(idade)

    print(cadastro)

    break