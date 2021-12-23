#A função socket() do módulo ‘socket’ de Python é responsável por criar um socket no processo tanto para protocolo TCP, quanto UDP. Como diferenciar se o socket a ser criado é TCP e UDP?

print("Para TCP:")
print("socket_family: família do socket. Pode ser  AF_INET (para IPv4 e é o padrão), AF_INET6 (para IPv6), AF_UNIX, AF_CAN ou AF_RDS (tipos de sockets Unix e Linux).")
print("socket_type: tipo do socket. Para TCP deve-se usar a constante socket.SOCK_STREAM, que é o valor padrão para a função.")

print("Para UDP:")
print("socket_family: família do socket. Pode ser  AF_INET (para IPv4 e é o padrão), AF_INET6 (para IPv6), AF_UNIX, AF_CAN ou AF_RDS (tipos de sockets Unix e Linux).")
print("socket_type: tipo do socket. Para UDP, deve-se usar a constante socket.SOCK_DGRAM.")
