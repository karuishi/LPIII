import threading
import time
import random

capacidade = 5
buffer = []
buffer = buffer[:capacidade]

condition = threading.Condition()

def produtor():
    for _ in range(10):
        time.sleep(1)
        with condition:
            while len(buffer) == capacidade: # Caso o buffer esteja cheio, a produção é parada
                condition.wait()           
            random_num = random.randint(1, 100)
            buffer.append(random_num)
            print(f"Número aleatório adicionado: {random_num}")
            condition.notify() # Notifica que a chave foi liberada para acesso
            
def consumidor():
    for _ in range(10):
        time.sleep(1)
        with condition:
            while len(buffer) == 0: # Caso o buffer esteja vazio, o consumo é parado
                condition.wait()
            num = buffer.pop(0)
            print(f"Número removido: {num}")
            condition.notify() # Notifica que a chave foi liberada para acesso
            
prod_thread = threading.Thread(target=produtor)
con_thread = threading.Thread(target=consumidor)

prod_thread.start()
con_thread.start()

prod_thread.join()
con_thread.join()