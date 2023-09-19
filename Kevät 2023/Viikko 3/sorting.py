import time
import random
alku = time.time()

def sort():
    taulu = []
    n = 10**5

    for _ in range(n):
        taulu.append(random.randint(1,n))

    print(taulu)

    for i in range(n):
        j = i-1
        while j >= 0 and taulu[j] > taulu[j+1]:
            taulu[j], taulu[j+1] = taulu[j+1], taulu[j]
            j -= 1
    
    return taulu

print(sort())

loppu = time.time()
print("aikaa kului", loppu-alku, "s (O(n)")