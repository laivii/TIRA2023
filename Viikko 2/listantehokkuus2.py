import time
lista = []

alku1 = time.time()

for i in range(1, 10**5+1):
    lista.append(i)

loppu1 = time.time()
print("lisäämisessä kesti: ", loppu1-alku1, "s")

alku2 = time.time()

for i in range(len(lista)):
    lista.remove(lista[0])

loppu2 = time.time()
print("poistamisessa kesti: ", loppu2-alku2, "s")

print(len(lista))