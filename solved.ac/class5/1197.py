import sys; read = sys.stdin.readline
import heapq

v, e = map(int, read().split())
graph = {i:[] for i in range(1, v+1)}
visited = [False] * (v+1)

for i in range(e):
    a, b, c = map(int, read().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

def prim(start):
    visited[start] = True
    candidate = graph[start]
    heapq.heapify(candidate)
    total_weight = 0

    while candidate:
        w, v = heapq.heappop(candidate)
        if not visited[v]:
            visited[v] = True
            total_weight += w

            for e in graph[v]:
                if not visited[e[1]]:
                    heapq.heappush(candidate, e)

    return total_weight

print(prim(1))

