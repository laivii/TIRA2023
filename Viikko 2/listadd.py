def create(t, x):
    lista = t
    pituus = len(lista)
    arvo = x
    päivitetty = []

    for i in range(pituus):
        uusi_arvo = lista[i]+arvo
        päivitetty.append(uusi_arvo)

    return päivitetty

if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]