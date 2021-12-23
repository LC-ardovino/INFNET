def diagnostico_mensal(renda_mensal,gastos_moradia,gastos_educacao,gastos_transporte):

    porcent_moradia = (gastos_moradia * 100)/renda_mensal
    gasto_moradia = (30*renda_mensal)/100
    porcent_educacao = (gastos_educacao * 100)/renda_mensal
    gasto_educacao = (20*renda_mensal)/100
    porcent_transporte = (gastos_transporte * 100)/renda_mensal
    gasto_transporte = (15*renda_mensal)/100

    print("Diagnóstico:")
    if porcent_moradia <= 30 and porcent_educacao <= 20 and porcent_transporte <= 15:
        print("Seus gastos estão dentro da margem recomendada.")
    if porcent_moradia > 30:
        print(f"Seus gastos totais com moradia comprometem {porcent_moradia}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_moradia}.")
    if porcent_moradia <= 30:
        print(f"Seus gastos totais com moradia comprometem {porcent_moradia}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.")
    if porcent_educacao > 20:
        print(f"Seus gastos totais com educação comprometem {porcent_educacao}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_educacao}.")
    if porcent_educacao <= 20:
        print(f"Seus gastos totais com educação comprometem {porcent_educacao}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.")
    if porcent_transporte > 15:
        print(f"Seus gastos totais com transporte comprometem {porcent_transporte}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {gasto_transporte}.")
    if porcent_transporte <= 15:
        print(f"Seus gastos totais com transporte comprometem {porcent_transporte}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.")


#Programa principal
renda_mensal = float(input("Renda mensal total: "))
gastos_moradia = float(input("Gastos totais com moradia: "))
gastos_educacao = float(input("Gastos totais com educação: "))
gastos_transporte = float(input("Gastos totais com transporte: "))

diagnostico_mensal(renda_mensal,gastos_moradia,gastos_educacao,gastos_transporte)
