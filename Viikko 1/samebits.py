def count(s):
    string = s
    ykköset = 0
    nollat = 0

    for i in range(len(string)):
        arvo = string[i]

        if arvo == "1":
            ykköset += 1
        else:
            nollat += 1

    if ykköset > nollat:
        return nollat
    else: 
        return ykköset


if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4