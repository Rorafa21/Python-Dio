cadastro = []
register = False

while register == True:
    
    nome = input("Qual seu nome?: ")
    cpf = int(input("Qual seu cpf?: "))
    idade = int(input("Qual sua idade?: "))

    cadastro.append(nome)
    cadastro.append(cpf)
    cadastro.append(idade)

    print(cadastro)

    break
###################################################################
nomes = ['Rodrigo', "Itamar", "Kel"]
cond = True

while cond == True:
    print(f"Ola {nomes[0]}")
    print(f"Ola {nomes[1]}")
    print(f"Ola {nomes[2]}")

    break
###################################################################

