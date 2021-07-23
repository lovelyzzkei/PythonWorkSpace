import sys; read = sys.stdin.readline
import heapq
from math import sqrt, pow

n = int(read())
INF = int(1e4)
d = [[INF for _ in range(n)] for __ in range(n)]
graph = {i:[] for i in range(n)}
stars = []
visited = [False] * n
for tc in range(n):
    stars.append(list(map(float, read().split())))

for i in range(n):
    for j in range(i+1):
        star1 = stars[i]; star2 = stars[j]
        dist = sqrt(pow(star1[0]-star2[0], 2)+pow(star1[1]-star2[1], 2))
        d[i][j] = dist
        d[j][i] = dist
    
for start in range(n):
    for end in range(n):
        if start != end:
            graph[start].append([d[start][end], end])

def prim(start):
    total_weight = 0
    visited[start] = True
    candidate = graph[start]
    heapq.heapify(candidate)

    while candidate:
        w, v = heapq.heappop(candidate)
        if not visited[v]:
            visited[v] = True
            total_weight += w

            for e in graph[v]:
                if not visited[e[1]]:
                    heapq.heappush(candidate, e)

    return total_weight

print(f'{prim(0):.2f}')