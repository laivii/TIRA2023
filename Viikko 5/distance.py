import math

def find(t, k):
    lista = t
    päätöspiste = k
    pisin = 0
    lisätty = False
    
    if päätöspiste not in lista:
        lista.append(päätöspiste+1)
        lisätty = True
    
    lista.append(0)
    lista = sorted(lista)
    
    for i in range(1, len(lista)):
        luku1 = lista[i-1]
        luku2 = lista[i]
        vastaus = 0
        etäisyys = luku2-luku1-1

        if luku1+1 != luku2 and luku1 != luku2:
            if luku1 != 0:
                vastaus = math.ceil(etäisyys/2)
            else:
                vastaus = etäisyys

            if i == len(lista)-1 and lisätty == True:
                vastaus = etäisyys

        if vastaus >= pisin:
            pisin = vastaus

    return pisin

if __name__ == "__main__":
    print(find([2, 11, 9, 10, 10], 15)) # 4
    #print(find([12, 3, 13, 14, 6], 15)) # 3
    #print(find([1, 2, 9], 11)) # 3
    #print(find([2, 1, 3], 3)) # 0
    #print(find([7, 4, 10, 4], 10)) # 3
    #print(find([15, 2, 6, 4, 18], 20)) # 4
    #print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970