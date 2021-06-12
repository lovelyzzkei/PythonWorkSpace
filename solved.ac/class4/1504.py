import heapq
import sys; input = sys.stdin.readline

n, e = map(int, input().split())

INF = int(1e9)
graph = {i:[] for i in range(1, n+1)}

def dijkstra(start, end):
    if start == end:
        return 0

    q = []
    d = [INF] * (n+1)   # 최단 경로 저장
    heapq.heappush(q, (start, 0))

    while q:
        now, dist = heapq.heappop(q)
        if d[now] < dist:   # 이미 경로가 해당 노드를 거쳐가는 것보다 짧다면 패스
            continue
        for next in graph[now]:      
            if end != n and next[0] == n:   # 아직 특정 정점을 거치지도 않았는데 최종 도착지에 가면 안됨
                continue
            cost = dist + next[1]
            if cost < d[next[0]]:
                d[next[0]] = cost
                heapq.heappush(q, (next[0], cost))
    
    return d[end]
    

# 간선 정보 저장
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())
if v1 == 1 and v2 == n:
    route = dijkstra(1, n)
elif v1 == 1:
    route = dijkstra(1, v2) + dijkstra(v2, n)
elif v2 == n:
    route = dijkstra(1, v1) + dijkstra(v1, n)
else:
    route = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n), \
        dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n))

# 갈 수 없는 경우 -1 출력
if route >= INF:
    print(-1)
else:
    print(route)