def find(t):
    lista = t
    pituus = len(lista)
    määrät = {}

    for i in range(pituus):
        arvo = lista[i]
        if arvo in määrät:
            määrät[arvo] += 1
        else:
            määrät[arvo] = 1

    for i in määrät:
        if määrät[i] == 1:
            return i

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5