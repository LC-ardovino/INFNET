nota = float(input("Digite a sua nota:"))

while nota<0 or nota>10:
    print("Nota inválida.")
    nota = float(input("Digite a sua nota:"))
print("Sua nota foi registrada com sucesso!")