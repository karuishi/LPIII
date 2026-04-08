import socket 

# Cria um objeto socket para comunicação UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
porta = 12345

# Envia uma mensagem para o servidor
mensagem = b'A' * 1024
cliente.sendto(mensagem, (host, porta))
print('Mensagem enviada para o servidor: ', mensagem)

# Receba a resposta do servidor
resposta, endereco_servidor = cliente.recvfrom(1024)
print('Resposta recebida do servidor:', resposta.decode())

# Fecha o socket
cliente.close()