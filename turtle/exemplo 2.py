import turtle

turtle.title("A tartaruga.")
turtle.shape("turtle")
distancia = int(input("Digite a distância que a tartaruga irá percorrer: "))
if distancia > 0:
    turtle.forward(distancia)
else:
    print("Distância inválida.")