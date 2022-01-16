import sys; read = sys.stdin.readline
from collections import deque

INF = sys.maxsize

n, m = map(int, read().split())

c = [[0 for i in range(n+1)] for j in range(n+1)]
f = [[0 for i in range(n+1)] for j in range(n+1)]

adj = [[] for i in range(n+1)]

for i in range(m):
    u, v, w = map(int, read().split())
    adj[u].append(v)
    adj[v].append(u)
    c[u][v] = w
    c[v][u] = w

s, t = map(int, read().split())

def maxFlow():
    totalFlow = 0

    while True:
        parent = [-1 for i in range(n+1)]
        parent[s] = s
        
        q = deque([s])

        while len(q) != 0 and parent[t] == -1:
            x = q.popleft()

            for y in adj[x]:
                if c[x][y] - f[x][y] > 0 and parent[y] == -1:
                    parent[y] = x
                    q.append(y)


        # s-t cut 발생
        if parent[t] == -1:
            break
        
        i = t
        flow = INF
        while i != s:
            flow = min(flow, c[parent[i]][i] - f[parent[i]][i])
            i = parent[i]

        i = t
        while i != s:
            f[parent[i]][i] += flow
            f[i][parent[i]] -= flow
            i = parent[i]
        
        totalFlow += flow

    return totalFlow


print(maxFlow())