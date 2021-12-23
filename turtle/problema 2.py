
maior = 0
for n in range(1,6):
    numero = int(input(f"Digite o {n}ºnúmero:"))
    if maior < numero:
        maior = numero
print(f"O maior número é {maior}")