# Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias e
# retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.
def idade_em_dias(anos,meses,dias):
    anos_completos = (anos-1)*365
    meses_em_dias = meses*30
    idade_em_dias = anos_completos+meses_em_dias+dias

    print(f"A sua idade expressa em dias é: {idade_em_dias}.")


#programa principal:

anos = int(input("Quantos anos você tem? "))
meses = int(input("Em que mês você está(digite de 1-12)? "))
if meses>12 or meses<1:
    print("O dado fornecido é inválido.")
    quit()
dias = int(input("Digite qual o dia de hj: "))
if dias> 30 or dias< 1:
    print("O dado fornecido é inválido.")
    quit()
idade_em_dias(anos,meses,dias)