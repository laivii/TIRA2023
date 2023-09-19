import collections

def solve(n,k):
    list = collections.deque([])

    for i in range(1,n+1):
        list.append(i)

    for j in range(k):
        list.append(list[1])
        list.append(list[0])
        list.popleft()
        list.popleft()
    
    newFirst = list[0]

    return newFirst

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875