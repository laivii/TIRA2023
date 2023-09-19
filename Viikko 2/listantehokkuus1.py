import time

n = 10**5
lista = []

alku1 = time.time()

for i in range(1, n+1):
    lista.append(i)

loppu1 = time.time()
print("aikaa kului lisäämiseen", loppu1-alku1, "s")

alku2 = time.time()

for i in range(n):
    lista.pop()

loppu2 = time.time()
print("aikaa kului poistamiseen", loppu2-alku2, "s")

