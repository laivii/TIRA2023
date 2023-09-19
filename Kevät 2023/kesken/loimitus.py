import random
def loimitus():
    taulu = []
    n = 10**5

    for _ in range(n):
        taulu.append(random.randint(1,n))

    for i in range(n):
        if taulu[i] == taulu[i+1]:
            return
        k = (taulu[i]+taulu[i+1])//2

    return taulu

print(loimitus())