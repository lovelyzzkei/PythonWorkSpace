import sys; read = sys.stdin.readline
import heapq
INF = int(1e8)

n, m = map(int, read().split())
d = [INF for i in range(n+1)]
graph = {i:[] for i in range(1, n+1)}
for tc in range(m):
    a, b, c = map(int, read().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
s, t = map(int, read().split())

def dijkstra(s, t):
    d[s] = 0
    edges = [[0, s]]
    heapq.heapify(edges)

    while edges:
        w, v = heapq.heappop(edges)
        if d[v] < w:
            continue
        for dist, child in graph[v]:
            cost = dist + d[v]
            if cost < d[child]:
                d[child] = cost
                heapq.heappush(edges, [cost, child])

dijkstra(s, t)
print(d[t])
