class Network:
    def __init__(self,n):
        self.n = n
        self.graph = {node: [] for node in range(1, n + 1)}

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self,a,b):
        self.distances = {}
        self.previous = {}

        self.distances[a] = 0
        self.previous[a] = None
        queue = [a]

        for node in queue:
            distance = self.distances[node]
            for next_node in self.graph[node]:
                if next_node not in self.distances:
                    self.distances[next_node] = distance + 1
                    self.previous[next_node] = node
                    queue.append(next_node)

        if b not in self.distances:
            return -1
        else:
            return self.distances[b]

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2