import threading

def increment_counter(lock):
    global counter
    for _ in range(1000000):
        # Assegura o lock
        lock.acquire()
        try:
            counter += 1
        finally:
            # Garante que o lock será liberado independentemente de erros
            lock.release()

counter = 0
lock = threading.Lock()

# Cria threads que compartilham o mesmo lock
thread1 = threading.Thread(target=increment_counter, args=(lock,))
thread2 = threading.Thread(target=increment_counter, args=(lock,))

# Inicia as threads
thread1.start()
thread2.start()

# Espera ambas threads completarem
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")