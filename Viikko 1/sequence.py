def generate(n):
    lukujono = [0]

    for i in range(11, 10000):
        luku = i
        uusiluku = str(luku)

        for j in range(len(uusiluku)):
            if uusiluku.count(uusiluku[j]) > 1:
                lukujono.append(luku)
                break

    return lukujono[n]

if __name__ == "__main__":
    print(generate(683)) # 11
    