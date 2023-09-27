def salvar_carro(marca, modelo, placa, ano):
    print(f"Carro salvo com sucesso! {marca},{modelo},{placa},{ano}")

#salvar_carro("Fiat", "Uno", "ABC-123", 1999)
#salvar_carro(marca = "Fiat", modelo = "Uno", placa = "ABC-123", ano = 1999)
salvar_carro(**{"marca" = "Fiat", "modelo" = ""})