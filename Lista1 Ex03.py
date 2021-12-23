altura = round(float(input("Digite a sua altura: ")), 2)
peso = int(input("Digite seu peso em kG: "))
IMC = round(peso/(altura**2), 2)
print(f"Seu IMC é {IMC}.")