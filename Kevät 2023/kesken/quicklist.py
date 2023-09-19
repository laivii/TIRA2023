import collections, itertools

class QuickList:
    def __init__(self, t):
        self.stack = collections.deque(t)
        self.start = 0
    
    def move(self, k):
        output = list(itertools.islice(self.stack, self.start, self.start+k))
        self.stack.extend(output)
        self.start += k
        
    def get(self, i):
        return self.stack[self.start + i]

if __name__ == "__main__":
    q = QuickList([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])
    q.move(6)
    q.move(7)
    print(q.get(1))
    print(q.get(6))
    print(q.get(4))
    q.move(6)
    q.move(8)
    q.move(3)
    print(q.get(9))
    print(q.get(9))