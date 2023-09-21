class MaxList:
    def __init__(self):
        self.stack = []
        self.suurin = [0]

    def add(self, x):
        suurin = self.suurin
        
        if x > suurin[0]:
            suurin[0] = x
            
        self.stack.append(x)

    def max(self):
        suurin = self.suurin
        
        if suurin[0] == 0:
            return "None"
        else:
            return suurin[0]

if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8