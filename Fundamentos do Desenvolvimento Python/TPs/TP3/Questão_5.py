#Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos).

def lista_maiores():
    soma = 0
    lista = []
    cont = 1
    while True:
        nome = str(input("Digite seu nome:"))
        if nome == "sair":
            print(lista)
            break
        altura = float(input("Digite sua altura:"))
        soma += altura
        media = soma / cont
        cont += 1
        if altura > media:
            lista.append(nome)

lista_maiores()









