def main():
    seq = [11,22,33,44,55]
    pilha = []
    for elemento in seq:
        pilha.append(elemento)
    while len(pilha) > 0:
        print(pilha)
        topo = pilha.pop()
        print("Objeto do topo: ", topo)

main()