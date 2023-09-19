def create(n):
    lista = []

    for i in range(1, n+1):
        lista.append(i)

    for i in range(len(lista)):
        if lista[i]%2 != 0:
            arvo = lista[i]
            lista.remove(arvo)
            lista.append(arvo)
        else:
            continue
        
    return lista

if __name__ == "__main__":
    print(create(4)) # [2, 1]
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]