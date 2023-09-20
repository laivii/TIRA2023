def count(s):
    merkkijono = s
    liikkeet = []
    sijainti = [0,0]
    ruudut = {"[0, 0]":1}


    for i in merkkijono:
        liikkeet.append(i)

    for i in range(len(liikkeet)):
        if liikkeet[i] == 'U':
            sijainti[0] += 1
        elif liikkeet[i] == 'D':
            sijainti[0] -= 1
        elif liikkeet[i] == 'L':
            sijainti[1] -= 1
        else:
            sijainti[1] += 1

        ruutu = str(sijainti)

        if ruutu not in ruudut:
            ruudut[ruutu] = 1

    return len(ruudut)

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2