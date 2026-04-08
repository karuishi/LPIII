import threading
import time

def thread_task(lock):
    global counter
    for _ in range(1000):
        # with lock:
        lock.acquire()
        try:
            counter += 1
        finally:
            lock.release()
            
counter = 0
lock = threading.Lock()

threads = []
for _ in range(10):
    thread = threading.Thread(target=thread_task, args=(lock,))
    threads.append(thread)
    thread.start()

for thread in threads: # Segundo laço para garantir a concorrẽncia 
    thread.join()

print(f"Final counter value: {counter}")