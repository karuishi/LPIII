import threading
import time

def print_numbers_cres():
    for number in range(1, 501):
        print(number)
        time.sleep(1)

def print_numbers_dec():
    for number in range(500, 0, -1):
        print(number)
        time.sleep(1)
        
thread1 = threading.Thread(target=print_numbers_cres)
thread2 = threading.Thread(target=print_numbers_dec)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas finalizadas")