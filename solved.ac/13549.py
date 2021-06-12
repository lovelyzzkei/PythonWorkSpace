import sys; read = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, end):
    q = []
    d = [INF] * 100001
    d[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        if d[now] < dist:
            continue
        cost = dist + 1
        if now+1 <= 100000 and cost < d[now+1]:
            d[now+1] = cost
            heapq.heappush(q, (cost, now+1))
        if now-1 >= 0 and cost < d[now-1]:
            d[now-1] = cost
            heapq.heappush(q, (cost, now-1))

        cost = dist
        if now*2 <= 100000 and cost < d[now*2]:
            d[now*2] = cost
            heapq.heappush(q, (cost, now*2))

n, k = map(int, read().split())
print(dijkstra(n, k))