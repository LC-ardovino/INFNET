import turtle

turtle.title("O quadrado.")
turtle.shape("turtle")
lado = int(input("Digite a distância do lado:"))
for n in range(4):
    turtle.forward(lado)
    turtle.left(90)