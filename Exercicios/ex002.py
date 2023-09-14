ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("ativos:"))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos = sorted(ativos)
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
print(ativos[0])
print(ativos[1])
print(ativos[2])
#descobrir porque não imprime corretamente os valores