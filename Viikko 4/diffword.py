def count(s):
    merkkijono = s
    lista = merkkijono.split(" ")
    sanat = {}

    for i in range(len(lista)):
        sana = lista[i]

        if sana not in sanat:
            sanat[sana] = 1

    return len(sanat)

if __name__ == "__main__":
    print(count("apina apina apina")) # 1
    print(count("apina banaani cembalo")) # 3
    print(count("a b c a b c a b c")) # 3
    print(count("saippuakauppias")) # 1