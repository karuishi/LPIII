import threading
import time

def print_numbers():
    for number in range(1, 6):
        print(number)
        #time.sleep(1)

# Cria a thread executando a função 'print_numbers'
thread = threading.Thread(target=print_numbers)
thread.start()

# Espere as threads terminarem
thread.join()
print("Thread finished execution.")

"""
P: O que acontece se o thread.join() for removido?

R: Enquanto a Thread Principal ainda está ocupada criando a Thread 4 e a 5, as Threads 1 e 2 já "nasceram", 
já começaram a rodar a função e já enviaram seus primeiros números para a tela!
"""