class QuickList:
    def __init__(self, t):
        self.stack = t
        self.indeksi = 0

    def move(self, k):
        self.indeksi += k

        if self.indeksi >= len(self.stack):
            määrä = self.indeksi%len(self.stack)
            self.indeksi = määrä
        
    def get(self, i):
        k = self.indeksi + i

        if k >= len(self.stack):
            määrä = k % len(self.stack)
            k = määrä

        return self.stack[k]

if __name__ == "__main__":
    q = QuickList(list(range(1, 10**5 + 1)))

    for i in range(10**5 - 1):
        q.move(10**5 - 1)

    print(q.get(10**4))