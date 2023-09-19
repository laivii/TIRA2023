import time
import random

lista = []

for i in range(10**7):
    numero = random.randint(0, 10**7)
    lista.append(numero)

alku1 = time.time()
# toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

count_even1(lista)

loppu1 = time.time()
print("aikaa kului toteutuksella 1:", loppu1-alku1, "s")

alku2 = time.time()

# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

count_even2(lista)

loppu2 = time.time()
print("aikaa kului toteutuksella 2:", loppu2-alku2, "s")