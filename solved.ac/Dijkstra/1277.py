import sys; read = sys.stdin.readline
import heapq
from math import sqrt, pow
INF = int(1e7)

n, w = map(int, read().split())
m = float(read())
powerPlant = {i:[] for i in range(1, n+1)}
MAP = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    powerPlant[i] = list(map(int, read().split()))

def uclid_dist(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

for plantA in range(1, n+1):
    for plantB in range(plantA, n+1):
        ax, ay = powerPlant[plantA]
        bx, by = powerPlant[plantB]
        MAP[plantA][plantB] = MAP[plantB][plantA] = uclid_dist(ax, ay, bx, by)

for i in range(w):
    u, v = map(int, read().split())
    MAP[u][v] = MAP[v][u] = 0

# for item in d:
#     print(item)

def dijkstra(start):
    d = {i:INF for i in range(1, n+1)}
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        if d[node] < dist:
            continue
        
        for child in range(1, n+1):
            if MAP[node][child] > m:
                continue
            cost = dist + MAP[node][child]
            if cost < d[child]:
                d[child] = cost
                heapq.heappush(q, (cost, child))

    return int(d[n]*1000)

print(dijkstra(1))