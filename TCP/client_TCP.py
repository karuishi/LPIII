import socket
import threading
import time

def simular_cliente(id_cliente):
    """Função que representa um único cliente conectando ao servidor."""
    try:
        # Cria o socket
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Endereço e porta corrigidos para baterem com o server.py
        host = '127.0.0.1' 
        porta = 65432      

        # Conecta-se ao servidor
        cliente.connect((host, porta))
        print(f'[Cliente {id_cliente}] Conectado ao servidor {host}:{porta}')

        # Envia algumas mensagens para testar o loop do servidor
        for i in range(3):
            mensagem = f'Olá do cliente {id_cliente}, esta é a mensagem {i+1}!'
            cliente.send(mensagem.encode('utf-8'))
            
            # Recebe a resposta do servidor
            resposta = cliente.recv(1024).decode('utf-8')
            print(f'[Cliente {id_cliente}] Recebeu: {resposta}')
            
            # Pausa de 1 segundo entre as mensagens para você ver o servidor trabalhando
            time.sleep(1) 

        # Fecha a conexão após terminar de enviar
        cliente.close()
        print(f'[Cliente {id_cliente}] Desconectou-se.')
        
    except ConnectionRefusedError:
        print(f'[Cliente {id_cliente}] Erro: O servidor não está rodando ou a porta está incorreta.')
    except Exception as e:
        print(f'[Cliente {id_cliente}] Erro inesperado: {e}')

# ==========================================
# Configuração do Teste
# ==========================================
NUM_CLIENTES = 5  # Mude este número para testar mais ou menos clientes ao mesmo tempo
threads = []

print(f"Iniciando simulação com {NUM_CLIENTES} clientes simultâneos...\n")

# Cria e inicia uma thread para cada cliente simulado
for i in range(NUM_CLIENTES):
    t = threading.Thread(target=simular_cliente, args=(i+1,))
    threads.append(t)
    t.start()
    time.sleep(0.2) # Um pequeno atraso só para as conexões não entrarem no exato mesmo milissegundo

# Aguarda todas as threads terminarem
for t in threads:
    t.join()

print("\nTodos os clientes terminaram o teste.")