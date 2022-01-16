import sys; read = sys.stdin.readline
from collections import deque

INF = sys.maxsize

n, m = map(int, read().split())

c = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
f = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
d = [[0 for i in range(n+m+2)] for j in range(n+m+2)]

adj = [[] for i in range(n+m+2)]

# 사람 - sink 연결
A = list(map(int, read().split()))
for i in range(n):
    c[m+i+1][m+n+1] = A[i]
    adj[m+i+1].append(m+n+1)

# source - 서점 연결
B = list(map(int, read().split()))
for i in range(m):
    c[0][i+1] = B[i]
    adj[0].append(i+1)

# 서점 - 사람 연결
for i in range(1, m+1):
    tmp = list(map(int, read().split()))
    for j in range(n):
        c[i][m+j+1] = tmp[j]
        if tmp[j] > 0:
            adj[i].append(m+j+1)

# 서점 - 사람 배송비 저장
for i in range(1, m+1):
    tmp = list(map(int, read().split()))
    for j in range(n):
        d[i][m+j+1] = tmp[j]
        d[m+j+1][i] = -tmp[j]


def maxFlow():
    totalFlow = 0
    totalDeliver = 0

    start = 0
    end = n + m + 1

    while True:
        parent = [-1 for i in range(end+1)]
        parent[start] = 0

        dist = [INF for i in range(end+1)]
        dist[start] = 0

        inQueue = [False for i in range(end+1)]
        
        q = deque([start])

        while len(q) != 0:
            x = q.popleft()
            inQueue[x] = False

            for y in adj[x]:
                if c[x][y] - f[x][y] > 0 and dist[x] + d[x][y] < dist[y]:
                    dist[y] = dist[x] + d[x][y]
                    parent[y] = x
                    if not inQueue[y]:
                        inQueue[y] = True
                        q.append(y)

        if parent[end] == -1:
            break

        i = end
        flow = INF
        while i != start:
            flow = min(flow, c[parent[i]][i] - f[parent[i]][i])
            i = parent[i]

        i = end
        while i != start:
            adj[i].append(parent[i])
            totalDeliver += flow * d[parent[i]][i]
            f[parent[i]][i] += flow
            f[i][parent[i]] -= flow

            i = parent[i]

        totalFlow += flow

    return totalFlow, totalDeliver


print("\n".join(str(x) for x in maxFlow()))