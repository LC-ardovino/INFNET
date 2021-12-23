import socket

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:

  # Tenta se conectar ao servidor
  s.connect(("192.168.50.8", 9999))
  msg = "Ola servidor!\n"
  # Envia mensagem codificada em bytes ao servidor
  s.send(msg.encode('ascii'))
  # Fecha conexão com o servidor
  s.close()
except Exception as erro:
  print(str(erro))