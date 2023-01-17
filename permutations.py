def count(a, b):
    pituus = len(a)
    jono1 = a
    jono2 = b
    indeksit = []
    aiemmin = 0

    for _ in range(pituus):
        indeksit.append([0,0])

    for i in range(pituus):
        luku = jono1[i]
        kohta = luku-1
        indeksit[kohta][0] = i+1

    for j in range(pituus):
        luku = jono2[j]
        kohta = luku-1
        indeksit[kohta][1] = j+1
    
    for k in range(pituus):
        if indeksit[k][0] < indeksit[k][1]:
            aiemmin += 1

    return aiemmin

if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5