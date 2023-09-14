saldo_atual = float(input("Saldo da conta: "))
valor_deposito = float(input("Valor de deposito: "))
valor_retirada = float(input("Valor de retirada: "))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual = (saldo_atual + valor_deposito) 
saldo_final = saldo_atual - valor_retirada
#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f"Saldo atualizado na conta: {saldo_final}")