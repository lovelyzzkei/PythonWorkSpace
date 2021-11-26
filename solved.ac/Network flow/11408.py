import sys; read = sys.stdin.readline
from collections import deque

MAX_NM = 802
INF = sys.maxsize

c = [[0 for i in range(MAX_NM)] for j in range(MAX_NM)]
f = [[0 for i in range(MAX_NM)] for j in range(MAX_NM)]
d = [[0 for i in range(MAX_NM)] for j in range(MAX_NM)]

n, m = map(int, read().split())

adj = [[] for j in range(n+m+2)]

def maxFlow():
    totalFlow = 0
    result = 0
    start = 0; end = n + m + 1

    while True:
        parent = [-1 for i in range(end + 1)]
        dist = [INF for i in range(end + 1)]

        parent[start] = 0
        dist[start] = 0

        inQueue = [False for i in range(end + 1)]
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
        
        # 최대 유량은 어차피 1 -> flow 탐색 과정은 생략
        totalFlow += 1
        
        i = end
        while i != start:
            result += d[parent[i]][i]
            f[parent[i]][i] += 1
            f[i][parent[i]] -= 1
            i = parent[i]

    return totalFlow, result


# 직원 - 일 연결
for i in range(n):
    work = list(map(int, read().split()))
    cnt = work[0]
    work = work[1:]

    for j in range(cnt):
        adj[i+1].append(n+work[2*j])
        adj[n+work[2*j]].append(i+1)
        c[i+1][n+work[2*j]] = 1
        
        d[i+1][n+work[2*j]] = work[2*j+1]
        d[n+work[2*j]][i+1] = -work[2*j+1]

# for i in range(n+m+2):
#     print(d[i][:n+m+2])

# source - 직원 연결
for i in range(n):
    adj[0].append(i+1)
    adj[i+1].append(0)
    c[0][i+1] = 1

# 일 - sink 연결
for i in range(m):
    adj[n+i+1].append(n+m+1)
    adj[n+m+1].append(n+i+1)
    c[n+i+1][n+m+1] = 1

print('\n'.join(str(x) for x in maxFlow()))