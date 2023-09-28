def somar(a ,b):
    return a + b
def subtrair (a, b):
    return a - b
def dividir (a, b):
    return a / b

def resultado_op (a , b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")

resultado_op(1, 20, somar)
resultado_op(1, 20, subtrair)
resultado_op(1, 20, dividir)

soma = somar
print(soma(1,2))