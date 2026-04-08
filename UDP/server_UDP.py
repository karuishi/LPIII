import socket

# Cria um objeto socket para comunicação UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereço e porta do servidor
host = 'localhost'
porta = 12345

# Associa o socket ao endereço e porta especificados
servidor.bind((host, porta))
print('Servidor UDP esperando por mensagens em {}:{}'.format(host, porta))

while True:
    # Receba a mensagem do cliente. Retorna também o endereço do cliente
    mensagem, endereco_cliente = servidor.recvfrom(512)
    print('Mensagem recebida:', mensagem.decode())
    
    # Envia uma resposta para o cliente
    resposta = 'Mensagem recebida pelo servidor'
    servidor.sendto(resposta.encode(), endereco_cliente)