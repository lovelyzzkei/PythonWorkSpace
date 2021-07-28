import sys; read = sys.stdin.readline
import heapq
INF = sys.maxsize

n, m = map(int, read().split())
ward = list(map(int, read().split()))
graph = {i:[] for i in range(n)}
d = {i:INF for i in range(n)}

for _ in range(m):
    a, b, t = map(int, read().split())
    graph[a].append([t, b])
    graph[b].append([t, a])
# print(ward)
# print(graph)
def dijkstra(start):
    d[start] = 0
    q = [[0, 0]]
    heapq.heapify(q)
    
    while q:
        dist, node = heapq.heappop(q)
        if d[node] < dist:
            continue
        for w, v in graph[node]:
            if v != n-1 and ward[v]:
                continue
            cost = dist + w
            if cost < d[v]:
                d[v] = cost
                heapq.heappush(q, [cost, v])

dijkstra(0)
if d[n-1] >= INF:
    print(-1)
else:
    print(d[n-1])