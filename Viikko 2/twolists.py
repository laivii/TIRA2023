def count(a, b):
    lista1 = a
    lista2 = b
    pituus = len(lista1)
    aiemmin = 0

    if lista1 == lista2:
        return aiemmin
    
    for i in range(pituus):
        arvo = lista1[i]
        paikka = lista2.index(arvo)

        if i < paikka:
            aiemmin += 1

    return aiemmin

if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5