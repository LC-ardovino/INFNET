genero = str(input("Digite uma das duas letras [F,M]:"))

if genero == 'F' or genero == 'f':
    print("F - Feminino")
elif genero == 'M' or genero == 'm':
    print("M-Masculino")
else:
    print("Outro gênero")