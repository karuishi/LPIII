import threading
import time

def worker():
    time.sleep(2)
    print("Hello from the thread!")
    
thread = threading.Thread(target=worker)
thread.start()
print("Em breve a thread vai executar um hello!")
thread.join()