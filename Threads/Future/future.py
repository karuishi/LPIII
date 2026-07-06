from concurrent.futures import ThreadPoolExecutor
import time

def sum_numbers(n):
    print(n)
    return 3

with ThreadPoolExecutor(max_workers=1) as executor:
    future= executor.submit(sum_numbers, 10)
    time.sleep(5)
    result = future.result()

print(result)