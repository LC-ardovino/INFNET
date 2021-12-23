#Para sockets UDP, responda:
#Que sequência de chamadas de funções em Python deve ser realizada pelo cliente? (Não precisa especificar os parâmetros)
#Que sequência de chamadas de funções em Python deve ser realizada pelo servidor? (Não precisa especificar os parâmetros)
#Quais destas funções são bloqueantes, isto é, o processo fica esperando?


print("UDP")
print("Lado Cliente")
print("socket()-Cria um socket, isto é, uma estrutura para controlar a comunicação em rede.")
print("bind()-Associa o socket a um endereço e porta de destino. Não é usado em Python no lado cliente, pois sendto já faz tal associação.")
print("sendto() e recvfrom()-Comunicação com o lado servidor.")
print("close()-Fecha uma conexão.")
print("----------------------------------------------------------------")

print("Lado Servidor")
print("socket()-Cria um socket (assim como no lado cliente).")
print("bind()-Associa o socket a um endereço e porta locais. Em Python, é necessário no lado servidor.")
print("sendto() e recvfrom()-Comunicação com o lado cliente.")
print("close()-Fecha uma conexão (assim como no lado cliente).")
