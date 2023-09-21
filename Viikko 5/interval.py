def count(t):
    luvut = sorted(t)
    peräkkäiset = 1
    max_määrä = 0

    if len(luvut) == 1:
        return 1

    for i in range(len(luvut)-1):
        luku1 = luvut[i]
        luku2 = luvut[i+1]

        if luku1+1 == luku2:
            peräkkäiset += 1

        if luku1+1 != luku2 or i == len(luvut)-2:
            if luku1 == luku2 and i != len(luvut)-2:
                continue
            else:
                if peräkkäiset >= max_määrä:
                    max_määrä = peräkkäiset

                peräkkäiset = 1

    return max_määrä

if __name__ == "__main__":
    print(count([80, 79, 51, 3, 6, 50, 52, 5, 35, 4, 51, 82, 53, 7, 81, 75, 78])) # 5
    print(count([18, 2, 17, 22, 3, 2, 11, 20, 21])) # 3
    print(count([14, 15, 16, 15, 13])) # 4
    print(count([15, 14, 9, 7, 10, 8])) # 4
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    a = list(range(10**6, 10**6 - 10**5, -1))
    print(count(a))