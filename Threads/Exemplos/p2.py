import threading
import time

def print_numbers():
    for number in range(1, 6):
        print(number)
        time.sleep(1)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(letter)
        time.sleep(1)

# Crie threads para cada função
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Inicie as threads
thread1.start()
thread2.start()

# Espera que as threads finalizem a execução
thread1.join()
thread2.join() #

print("As threads terminaram")

# P: Porque o print estão aparecendo de forma quase perfeitamente síncrona?
# R: Todas elas chegam na instrução time.sleep() (ou na tarefa de I/O) praticamente juntas e esperam a exata mesma quantidade de tempo