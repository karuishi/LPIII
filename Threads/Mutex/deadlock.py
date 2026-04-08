import threading
import time

# Dois recursos que serão adquirios pelas threads
lock1 = threading.Lock()
lock2 = threading.Lock()

# Função executada pela thread 1
def thread1_routine():
    lock1.acquire() # Adquire o primeiro recurso
    print("Thread 1 adquiriu lock1")
    
    # Simula algum processamento
    time.sleep(1)
    
    lock2.acquire() # Tenta adquirir o segundo recurso
    print("Thread 1 adquiriu lock2")
    
    # Libera os recursos
    lock2.release()
    lock1.release()
    
# Função executada pela thread 2
def thread2_routine():
    lock2.acquire() # Adquire o segundo recurso
    print("Thread 2 adquiriu o lock2")
    
    # Simula algum processamento
    time.sleep(1)
    
    lock1.acquire() # Tenta adquirir o primeiro recurso
    print("Thread 2 adquiriu lock1")
    
    # Libera os recursos
    lock1.release()
    lock2.release()
    
# Cria e inicia as threads
t1 = threading.Thread(target=thread1_routine)
t2 = threading.Thread(target=thread2_routine)

t1.start()
t2.start()

t1.join()
t2.join()