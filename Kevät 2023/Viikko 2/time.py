import time
import random

input = []

for _ in range(0, 100000):
    input += str(random.randint(0,1))

# O(n^2)
alku = time.time()

laskuri1 = 0
for i in range(0, len(input)):
    for j in range(1, len(input)):
        if input[i] == "0" and input[j] == "1":
            laskuri1 += 1

loppu = time.time()
print("aikaa kului", loppu-alku, "s (O(n^2)")

# O(n)
alku = time.time()

laskuri2 = 0
nollat = 0
for i in range(len(input)):
    if input[i] == "0":
        nollat += 1
    else:
        laskuri2 += nollat

loppu = time.time()
print("aikaa kului", loppu-alku, "s (O(n)")