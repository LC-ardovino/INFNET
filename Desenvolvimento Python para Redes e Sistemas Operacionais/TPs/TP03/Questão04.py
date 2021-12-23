#Para sockets TCP, responda:
#Que sequência de chamadas de funções em Python deve ser realizada pelo cliente? (Não precisa especificar os parâmetros)
#Que sequência de chamadas de funções em Python deve ser realizada pelo servidor? (Não precisa especificar os parâmetros)
#Quais destas funções são bloqueantes, isto é, o processo fica esperando?
print("TCP")
print("Lado cliente:")
print("socket()-cria um socket, isto é, uma estrutura para controlar a conexão em rede.")
print("connect()-conecta o socket local a um socket remoto (conexão com o servidor). É necessário especificar o IP (ou nome do servidor) e a porta de conexão.")
print("send() e recv() -comunicação com o lado servidor.")
print("close()-fecha uma conexão.")

print("---------------------------------------------------")

print("Lado servidor:")
print("socket()-Cria um socket (assim como no lado cliente).")
print("bind()-Associa o socket a um endereço e porta locais.")
print("listen()-permite que o socket aceite conexões.")
print("accept()-aceita a conexão de um cliente. Está associado ao connect() do lado cliente.")
print("send() e recv()-comunicação com o lado servidor (assim como no lado cliente).")
print("close()-fecha uma conexão (assim como no lado cliente).")
