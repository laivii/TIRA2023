class FastMode:
    def __init__(self):
        self.count = {}
        self.status = (0, 0)

    def add(self, x, k):
        if x not in self.count:
            self.count[x] = 0
        
        self.count[x] += k

        if self.status[0] == self.count[x] and x < self.status[1]:
            self.status = (self.count[x], x)
        elif self.status[0] != self.count[x]:
            self.status = max(self.status, (self.count[x], x))
        

    def mode(self):
        return self.status[1]

if __name__ == "__main__":
    f = FastMode()
    f.add(7, 5)
    print(f.mode())
    f.add(1, 6)
    print(f.mode())
    f.add(10, 2)
    print(f.mode())
    f.add(8, 4)
    print(f.mode())
    f.add(3, 6)
    print(f.mode())
    f.add(10, 8)
    print(f.mode())
    f.add(10, 5)
    print(f.mode())
    f.add(4, 9)
    print(f.mode())
    f.add(2, 9)
    print(f.mode())
    f.add(10, 10)
    print(f.mode())