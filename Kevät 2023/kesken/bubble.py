def count(t):
    kierrokset = 0
    tila = 0

    while True:
        change = False
        tila = 0
        for i in range(len(t)-1):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
                change = True
                tila = 1
            if change == True and tila != 1:
                    kierrokset += 1
        if not change:
            break
    
    return kierrokset

if __name__ == "__main__":
    print(count([1, 2, 3])) # 0
    print(count([2, 3, 4, 1])) # 3
    print(count([5, 1, 2, 3, 4])) # 1
    print(count([6, 2, 4, 1, 5, 3])) # 3
    print(count([2, 7, 4, 1, 9, 3, 8, 6, 5, 10])) # 4