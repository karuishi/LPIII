import threading
import time
import random

capacidade = 5
buffer = []
buffer = buffer[:capacidade]

condition = threading.Condition()

def produtor(id_produtor):
    for _ in range(10):
        time.sleep(random.uniform(0.1, 1.0))
        with condition:
            while len(buffer) == capacidade: # Caso o buffer esteja cheio, a produção é parada
                condition.wait()           
            random_num = random.randint(1, 100)
            buffer.append(random_num)
            print(f"Produtor {id_produtor} adicionou: {random_num}")
            condition.notify() # Notifica que a chave foi liberada para acesso
            
def consumidor(id_consumidor):
    for _ in range(10):
        time.sleep(random.uniform(0.1, 1.0))
        with condition:
            while len(buffer) == 0: # Caso o buffer esteja vazio, o consumo é parado
                condition.wait()
            num = buffer.pop(0)
            print(f"Consumidor {id_consumidor} removeu: {num}")
            condition.notify() # Notifica que a chave foi liberada para acesso
            
prod_threads = []
cons_threads = []
for i in range(3):
    thread = threading.Thread(target=produtor, args=(i,))
    prod_threads.append(thread)
    thread.start()
    
for i in range(3):
    thread = threading.Thread(target=consumidor, args=(i,))
    cons_threads.append(thread)
    thread.start()

for thread in prod_threads:
    thread.join()
    
for thread in cons_threads:
    thread.join()