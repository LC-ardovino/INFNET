n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
n3 = int(input("Digite a terceira nota:"))
media = round((n1+n2+n3)/3, 2)

if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
    print(f"Sua média será {media}.")
else:
    print("Informe notas válidas.")