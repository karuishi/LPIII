import threading
import time 

def increment_counter():
    global counter
    for _ in range(100000):
        temp = counter
        time.sleep(0.00001) # Talvez force uma mudança de thread
        counter = temp + 1

counter = 0

# Cria threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Inicia as threads
thread1.start()
thread2.start()

# Espera ambas completarem
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")

"""
Uma operação simples como contador += 1 parece instantânea, mas para o computador, ela tem três etapas:

Ler o valor atual (ex: 50).

Somar 1 (ex: 50 + 1 = 51).

Salvar o novo valor (51).

Sem o Lock para trancar a porta, a Thread 1 pode ler o valor "50" e, antes de ela conseguir salvar o "51", 
o sistema operacional passa o controle para a Thread 2. A Thread 2 também lê o valor "50", soma e salva "51". 
Quando a Thread 1 volta, ela simplesmente salva o seu "51" por cima. Duas threads fizeram o trabalho, mas o contador só subiu uma unidade!

"""
