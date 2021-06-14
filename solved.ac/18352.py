import sys; read = sys.stdin.readline
import heapq

def dijkstra(start, k):
    d = [INF] * (n+1)
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for v, w in graph[now]:
            cost = d[now] + w
            if cost < d[v]:
                d[v] = cost
                heapq.heappush(q, (cost, v))

    ret = []
    for i in range(1, n+1):
        if d[i] == k:
            ret.append(i)
    
    if ret:
        print('\n'.join(str(x) for x in ret))
    else:
        print(-1)




n, m, k, x = map(int, read().split())
graph = {i:[] for i in range(1, n+1)}; INF = int(1e8)
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append([b, 1])

dijkstra(x, k)