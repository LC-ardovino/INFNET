import subprocess

#subprocess.run é um comendo que recebe o nome do processo que será rodado.
print(subprocess.run("calc"))

#Exemplo 2:
print(subprocess.run(["notepad", "arq_texto.txt"]))

#Esta função recebe parâmetros semelhantes a subprocess.run(), mas o seu retorno é diferente. Ela retorna um objeto que, através dele, diversos atributos e funções relacionadas ao processo criado podem ser acessados.
p = subprocess.Popen("calc")
print("PID do processo criado:", p.pid)