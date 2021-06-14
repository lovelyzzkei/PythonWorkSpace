import sys; read = sys.stdin.readline

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def printDist(self, d):
        INF = int(1e9)
        for i in range(2, self.V+1):
            if d[i] == INF:     # 경로 없는 경우
                print(-1)
            else:
                print(d[i])

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, start):
        INF = int(1e9)
        d = [INF] * (self.V + 1)
        d[start] = 0

        for _ in range(self.V):
            for u, v, w in self.graph:
                if d[u] != INF and d[u] + w < d[v]:
                    d[v] = d[u] + w
                    if _ == self.V - 1:     # 음수 사이클 존재
                        print(-1)
                        return
        
        self.printDist(d)
        

n, m = map(int, read().split())
g = Graph(n)

for i in range(m):
    u, v, w = map(int, read().split())
    g.addEdge(u, v, w)

g.BellmanFord(1)

