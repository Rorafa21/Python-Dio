def somar (numeros):
    return sum(numeros)
    

print(somar([2,4,5]))


def retorna_sucessor_e_antecessor (numero):
    sucessor = numero + 1
    antecessor = numero -1
    return antecessor, sucessor

print(retorna_sucessor_e_antecessor(15))