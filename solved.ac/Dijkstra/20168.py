import sys; read = sys.stdin.readline
import heapq

n, m, a, b, c = map(int, read().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u].append([w, v])
    graph[v].append([w, u])

def dijkstra(start, end, money):
    INF = int(1e8)
    d = [INF] * (n+1)
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start, 0))    # (수금액, 출발 지점, 최대 수치심)
    ans = INF

    while q:
        dist, node, shame = heapq.heappop(q)
        if node == end:
            if dist <= money:
                ans = min(ans, shame)
        
        # if d[node] < dist:
        #     continue

        for w, child in graph[node]:
            cost = dist + w
            if cost < d[child]:
                d[child] = cost
                heapq.heappush(q, (cost, child, max(shame, w)))

        # print(d)
    if ans == INF:
        return -1
    else:
        return ans

print(dijkstra(a, b, c))