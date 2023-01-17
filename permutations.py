def count(a, b):
    indeksit = []
    aiemmin = 0

    for _ in range(len(a)):
        indeksit.append([0])

    for i in range(len(a)):
        luku = a[i]
        kohta = luku-1
        indeksit[kohta] = i+1

    for j in range(len(b)):
        luku = b[j]
        kohta = luku-1
        if indeksit[kohta] < j+1:
            aiemmin += 1

    return aiemmin

if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5