class Cities:
    def __init__(self,n):
        self.n = n
        self.graph = {node: [] for node in range(1, n + 1)}

    def add_road(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)

        #print(self.graph)
    
    def has_route(self,a,b):
        self.visited = set()
        self.visit(a)

        if b in self.visited:
            return True
        else:
            return False

    def visit(self, a):
        if a in self.visited:
            return
        #print("visit node", a)
        self.visited.add(a)

        for next_node in self.graph[a]:
            self.visit(next_node)
         

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True