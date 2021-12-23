import turtle

turtle.title("Desenho.")
turtle.shape("turtle")
angulo = 0

while angulo >= 0:
    lado = int(input("Digite o comprimento do lado:"))
    angulo = int(input("Digite o ângulo desejado:"))
    turtle.forward(lado)
    turtle.left(angulo)