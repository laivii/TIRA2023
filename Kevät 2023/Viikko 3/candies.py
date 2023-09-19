def solve(prices, x):
    n = len(prices)
    summa = 0
    määrä = 0
    prices.sort()

    for i in range(n):
        summa += prices[i]
        if summa <= x:
            määrä += 1

    return määrä

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1