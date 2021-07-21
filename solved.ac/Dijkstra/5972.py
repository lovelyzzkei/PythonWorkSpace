import sys; read = sys.stdin.readline
import heapq

n, m = map(int, read().split())
INF = int(1e8)
d = [INF for _ in range(n+1)]
farm = {i:[] for i in range(1, n+1)}

for tc in range(m):
    a, b, c = map(int, read().split())
    farm[a].append([b, c])
    farm[b].append([a, c])

# print(farm)
def dijkstra(start):
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))   # (cost, node) 순으로 저장

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue

        for child, cows in farm[now]:
            cost = dist + cows
            if cost < d[child]:
                d[child] = cost
                heapq.heappush(q, (cost, child))
    # for item in d:
    #     print(item)

dijkstra(1)
print(d[n])