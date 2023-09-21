class RepeatList:
    def __init__(self):
        self.stack = {}
        self.useita = False

    def add(self, x):
        if x not in self.stack:
            self.stack[x] = 1
        else:
            self.stack[x] += 1
            self.useita = True

    def check(self):
        if self.useita == True:
            return True
        else:
            return False

if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True