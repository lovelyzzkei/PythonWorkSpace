import sys; read = sys.stdin.readline
import heapq
from math import sqrt, pow
INF = int(1e8)

n, f = map(int, read().split())
nodes = [[0, 0]]
graph = {i:[] for i in range(1, n+1)}
for _ in range(n):
    x, y = map(int, read().split())
    for idx, node in enumerate(nodes):
        
    nodes.append([x, y])

def dijkstra(start):
    d = [INF for i in range(n+1)]
    q = []
    heapq.heappush(q, (0, 0))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        cx, cy = nodes[now]
        for nxt, child in enumerate(nodes):
            nx, ny = child
            if abs(ny-cy) <= 2 and abs(nx-cx) <= 2:
                w = sqrt(pow(ny-cy, 2) + pow(nx-cx, 2))
                if dist + w < d[nxt]:
                    d[nxt] = dist + w
                    heapq.heappush(q, (dist + w, nxt))
    
    ans = INF
    for idx, node in enumerate(nodes):
        if node[1] == f:
            ans = min(ans, d[idx])
    
    return int(round(ans, 0))

print(dijkstra(0))