import sys; read = sys.stdin.readline
from collections import deque

MAX_NM = 202
INF = sys.maxsize

c = [[0 for i in range(MAX_NM)] for j in range(MAX_NM)]
f = [[0 for i in range(MAX_NM)] for j in range(MAX_NM)]
d = [[0 for i in range(MAX_NM)] for j in range(MAX_NM)]


n, m = map(int, read().split())

adj = {i:[] for i in range(n+m+2)}

# 사람 - sink 연결
a = list(map(int, read().split()))

for i in range(n):
    adj[m+i+1].append(m+n+1)
    c[m+i+1][m+n+1] = a[i]

# source - 서점 연결
b = list(map(int, read().split()))

for i in range(m):
    adj[0].append(i+1)
    c[0][i+1] = b[i]

# 서점 - 사람 연결
for i in range(m):
    cost_ij = list(map(int, read().split()))
    
    for j in range(n):
        d[i+1][m+j+1] = cost_ij[j]      # 정방향 간선 비용
        d[m+j+1][i+1] = -cost_ij[j]     # 역방향 간선 비용
        c[i+1][m+j+1] = INF
        adj[i+1].append(m+j+1)
    
# 최소 비용 최대 유량 탐색
def maxFlow():
    result = 0
    start = 0
    end = n + m + 1

    while True:
        parent = [-1 for i in range(end+1)]
        dist = [INF for i in range(end+1)]

        parent[start] = 0
        dist[start] = 0
        
        # 정점 v가 이미 큐 안에 있는지 확인하기 위한 큐
        inQueue = [False for i in range(end+1)]
        
        # BFS를 위한 큐
        q = deque([start])

        # BFS 수행, 최단경로 탐색
        while len(q) != 0:
            x = q.pop()
            inQueue[x] = False

            # x에서 갈 수 있는 노드들 중 최단 거리로 갈 수 있는 노드들에 대하여 탐색
            # FF나 Edmond-karp 와는 달리 sink에 도달하였어도 최단 거리 탐색을 위하여 계속해서 갱신
            for y in adj[x]:
                if c[x][y] - f[x][y] > 0 and dist[x] + d[x][y] < dist[y]:
                    dist[y] = dist[x] + d[x][y]
                    parent[y] = x
                    if not inQueue[y]:
                        inQueue[y] = True
                        q.append(y)

        # 더 이상 경로가 없으면 함수 종료
        if parent[end] == -1:
            break

        # AUGMENTING FLOW
        flow = INF
        i = end
        while i != start:
            flow = min(flow, c[parent[i]][i] - f[parent[i]][i])
            i = parent[i]

        i = end
        while i != start:
            adj[i].append(parent[i])
            result += flow * d[parent[i]][i]    # 각 간선의 비용만큼 전체 비용 증가
            f[parent[i]][i] += flow
            f[i][parent[i]] -= flow
            i = parent[i]
        
    return result

print(maxFlow())

        