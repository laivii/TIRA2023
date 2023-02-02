def count(t):
    jono = sorted(t)
    jono = list(dict.fromkeys(jono))
    n = len(jono)
    laskuri = 1
    tulokset = []

    for i in range(n):
        #print(jono, jono[i-1], jono[i])
        if i != 0 and jono[i-1] == jono[i]-1:
            laskuri += 1
        else:
            laskuri = 1
        tulokset.append(laskuri)

    tulokset.sort()
    tulokset.reverse()

    return tulokset[0]

if __name__ == "__main__":
    print(count([14, 15, 16, 15, 13])) # 4
    print(count([15, 14, 9, 7, 10, 8])) # 4
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3