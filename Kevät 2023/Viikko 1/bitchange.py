def create(n, k):
    bittijono = []

    for _ in range(n):
        bittijono.append("0")

    for _ in range(k):
        for i in range(len(bittijono)):
            bitti = bittijono[i]
            if bitti == "0":
                bittijono[i] = "1"
                break
            else:
                bittijono[i] = "0"

    return "".join(bittijono)

if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111