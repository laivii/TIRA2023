def count(t):
    lista = t
    pituus = len(lista)

    if pituus == 0:
        return 0

    lista = str(lista)

    lista = lista.replace("[", "").replace(",", "").replace("]", "").split(" ")

    return len(lista)



if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8
    print(count([2, [81]])) # 2
    print(count([])) # 0