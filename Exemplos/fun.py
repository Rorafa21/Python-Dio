def exibir_mensagem():
    print("OLa Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}\n")

def ex_men_3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}\n")

exibir_mensagem()

exibir_mensagem_2("Rodrigo")

ex_men_3('rafa')
ex_men_3()