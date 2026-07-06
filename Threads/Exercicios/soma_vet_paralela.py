from concurrent.futures import ThreadPoolExecutor
import time
import random

tam_vetor = 100
tam_pedaco = 20
vetor = [random.randint(1, 100) for _ in range(tam_vetor)]
print(f"{vetor[:20]} ...")

def somar_parte(sub_vetor):
    return sum(sub_vetor)

futures = []
soma_total = 0
with ThreadPoolExecutor() as executor:
    for i in range(0, len(vetor), tam_pedaco):
        pedaco = vetor[i : i + tam_pedaco]
        future = executor.submit(somar_parte, pedaco)
        futures.append(future)
    
    for future in futures:
        result = future.result()
        soma_total += result

print(f"A soma total do vetor é: {soma_total}")