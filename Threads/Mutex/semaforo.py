import threading
import time
sem = threading.Semaphore(value=2)

def fun1():
    sem.acquire()
    for i in range(5):
        print(1)
        time.sleep(0.25)
    sem.release()

def fun2():
    sem.acquire()
    for i in range(5):
        print(2)
        time.sleep(0.25)
    sem.release()

def fun3():
    for i in range(5):
        sem.acquire()
        print(3)
        sem.release()
        time.sleep(0.25)

t = threading.Thread(target = fun1)
t2 = threading.Thread(target = fun2)
t3 = threading.Thread(target = fun3)
t.start()
t2.start()
t3.start()
t.join()
t2.join()
t3.join()
