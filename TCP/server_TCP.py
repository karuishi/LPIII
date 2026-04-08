import socket
import time

# 1. Configuração inicial do socket
HOST = '127.0.0.1'
PORT = 65432
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

# 2. Tornar o servidor não-bloqueante
servidor.setblocking(False)
print(f"Servidor a escutar em {HOST}:{PORT} (Modo Não-Bloqueante)")

clientes = [] # Lista para guardar os sockets dos clientes ligados

# 3. Laço principal do servidor
while True:
    # --- FASE A: Tentar aceitar novos clientes ---
    try:
        cliente, endereco = servidor.accept()
        print(f"Nova ligação de {endereco}")
        clientes.append(cliente) # Adiciona o novo cliente à lista
    except BlockingIOError:
        pass # Ninguém a tentar ligar neste momento

    # --- FASE B: Processar os clientes já ligados ---
    for cliente in clientes[:]: # Usamos [:] para iterar sobre uma cópia da lista e poder removê-los com segurança
        try:
            mensagem = cliente.recv(1024)
            
            if not mensagem:
                # Recebemos b'', o que significa que o cliente se desligou
                print("Um cliente desligou-se.")
                clientes.remove(cliente)
                cliente.close()
            else:
                # Recebemos dados reais, processamos e respondemos
                texto = mensagem.decode('utf-8')
                print(f"Recebido: {texto}")
                resposta = "Mensagem recebida!".encode('utf-8')
                cliente.send(resposta)
                
        except BlockingIOError:
            pass # Este cliente não enviou nada neste milissegundo

    # Pequena pausa para não sobrecarregar o processador (10 milissegundos)
    time.sleep(0.01)