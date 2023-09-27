valor_inicial = int(input())
taxa_juros = float(input())
periodo = int(input())

def calculo_juros(valor_inicial, taxa_juros,periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    valor_final = round(valor_final,2)
    return valor_final
    
resultado_final = calculo_juros(valor_inicial, taxa_juros, periodo)
print(f"Valor final do investimento: R$ {resultado_final}")