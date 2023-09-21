def find(t):
    lista = t
    sijainnit = {}
    pisin = 0

    for i in range(len(lista)):
        luku = lista[i]

        if luku not in sijainnit:
            sijainnit[luku] = [i, 0]
        else:
            sijainnit[luku][1] = i
    
    for i in sijainnit:
        kohdat = sijainnit[i]
        etäisyys = kohdat[1]-kohdat[0]

        if etäisyys >= pisin:
            pisin = etäisyys
    
    return pisin

if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4