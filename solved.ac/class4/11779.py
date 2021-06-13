import sys; read = sys.stdin.readline
import heapq

def dijkstra(start, end):
    q = []
    d = [INF] * (n+1)
    d[start] = 0
    heapq.heappush(q, (0, start, [start]))  # 비용, 시작점, 경로

    while q:
        dist, now, path = heapq.heappop(q)
        if d[now] < dist:
            continue

        for next in city[now]:
            cost = dist + next[1]
            if cost < d[next[0]]:
                d[next[0]] = cost
                npath = path + [next[0]]
                if next[0] == end:
                    ans = npath
                heapq.heappush(q, (cost, next[0], npath))
        
    return [d[end], len(ans), " ".join(str(x) for x in ans)]


n = int(read())
m = int(read())

INF = int(1e9)
city = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, read().split())
    city[a].append([b, c])

start, end = map(int, read().split())
ret = dijkstra(start, end)
print('\n'.join(str(x) for x in ret))