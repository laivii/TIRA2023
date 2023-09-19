import time
import collections

list = collections.deque([])
n = 10**5

#Lukujen lisääminen
alku = time.time()

for i in range(1,n+1):
    list.append(i)

loppu = time.time()
print("aikaa kului lisäämiseen", loppu-alku, "s")

#Lukujen poistaminen
alku2 = time.time()

for i in range(n):
    list.pop()

loppu2 = time.time()
print("aikaa kului poistamiseen", loppu2-alku2, "s")