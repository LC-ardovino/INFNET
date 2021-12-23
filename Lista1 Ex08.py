salario = float(input("Digite seu salário: "))
reajuste = float(input("Digite o reajuste salarial desejado: "))
print(f"O novo salário é {round((salario*reajuste)/100+salario, 2)}$")