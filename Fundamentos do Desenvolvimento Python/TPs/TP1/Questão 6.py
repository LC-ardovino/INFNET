# Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa
# tupla e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste
# caso, retorne qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário
# que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo deve ser menor
# do que a soma do comprimento dos outros dois lados. Além disso, o programa deve identificar o tipo de
# triângulo formado observando as seguintes definições:


def triangulos(X,Y,Z, triangulo):
    if X > Y+Z or Y > X+Z or Z > X+Y:
        print("Valores inválidos.")
        exit()
    elif X == Y == Z:
        print("Triângulo Equilátero")
    elif X == Y or X==Z or Y==Z:
        print("Triângulo Isósceles")
    elif X != Y and X != Z and Z != Y:
        print("Triângulo Escaleno")
    triangulo =(X,Y,Z)
    print(triangulo)
#PROGRAMA PRINCIPAL

X = float(input("Digite o comprimento do lado X do triângulo: "))
Y = float(input("Digite o comprimento do lado Y do triângulo: "))
Z = float(input("Digite o comprimento do lado Z do triângulo: "))
triangulo = tuple
triangulos(X,Y,Z, triangulo)
