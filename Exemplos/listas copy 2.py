convidados = ["Rodrigo", "Itamar", "Kel"]
print("##########################################################\n")
print(f"{convidados[0]} você foi convidado para o jantar especial!")
print(f"{convidados[1]} você foi convidado para o jantar especial!")
print(f"{convidados[2]} você foi convidado para o jantar especial!")

print("##########################################################\n")

convidados[2] = "Nicole" 
print("Kel não podera comparecer.")

print("##########################################################\n")

print(f"{convidados[0]} você foi convidado para o jantar especial!")
print(f"{convidados[1]} você foi convidado para o jantar especial!")
print(f"{convidados[2]} você foi convidado para o jantar especial!")

print("##########################################################\n")

print("Encontramos mais uma mesa para mais 3 convidados: Rafa, Sara, Gui")

print("##########################################################\n")

convidados.insert(0, "Rafa")
convidados.insert(1, "Sara")
convidados.append("Gui")

print(f"{convidados[0]} você foi convidado para o jantar especial!")
print(f"{convidados[1]} você foi convidado para o jantar especial!")
print(f"{convidados[2]} você foi convidado para o jantar especial!")
print(f"{convidados[3]} você foi convidado para o jantar especial!")
print(f"{convidados[4]} você foi convidado para o jantar especial!")
print(f"{convidados[5]} você foi convidado para o jantar especial!")

print("##########################################################\n")

print("Houve imprevistos e sera possivel convidar apenas 2 (duas) pessoas para o jantar ;-;")
print("##########################################################\n")
convidados_retirados = convidados.pop()
print(f"{convidados_retirados} Desculpa mas você não foi selecionado para o jantar ;-;")
convidados_retirados = convidados.pop()
print(f"{convidados_retirados} Desculpa mas você não foi selecionado para o jantar ;-;")
convidados_retirados = convidados.pop()
print(f"{convidados_retirados} Desculpa mas você não foi selecionado para o jantar ;-;")
convidados_retirados = convidados.pop()
print(f"{convidados_retirados} Desculpa mas você não foi selecionado para o jantar ;-;")
print("##########################################################\n")
print(f"{convidados[0]} você foi selecionado(a) para o jantar :D")
print(f"{convidados[1]} você foi selecionado(a) para o jantar :D")
print("##########################################################\n")

del convidados[0:]
print(convidados)
