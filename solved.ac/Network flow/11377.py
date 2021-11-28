import sys;read = sys.stdin.readline
from collections import deque

n, m, k = map(int, read().split())

c = [[0 for i in range(n+m+3)] for j in range(n+m+3)]
f = [[0 for i in range(n+m+3)] for j in range(n+m+3)]
adj = [[] for i in range(n+m+3)]

R = [0 for i in range(n+m+3)]

# source - 직원 연결
# 추가 source - 직원 연결
adj[0].append(n+m+2)
c[0][n+m+2] = k

for i in range(n):
    adj[0].append(i+1)
    adj[n+m+2].append(i+1)
    
    c[0][i+1] = 1
    c[n+m+2][i+1] = 1

# 직원 - 일 연결
for i in range(n):
    work_ij = list(map(int, read().split()))
    for j in range(1, work_ij[0]+1):
        adj[i+1].append(work_ij[j] + n)
        c[i+1][work_ij[j] + n] = 1

# 일 - sink 연결
for i in range(m):
    adj[n+i+1].append(n+m+1)
    c[n+i+1][n+m+1] = 1


def maxFlow():
    totalFlow = 0
    start = 0; end = n + m + 1

    while True:
        parent = [-1 for i in range(end+2)]
        parent[0] = 0

        inQueue = [False for i in range(end+2)]

        q = deque([start])

        while len(q) != 0:
            x = q.popleft()
            inQueue[x] = False

            for y in adj[x]:
                if c[x][y] - f[x][y] > 0 and parent[y] == -1:
                    if not inQueue[y]:
                        parent[y] = x
                        q.append(y)

                        if y == end:
                            break

        if parent[end] == -1:
            break

        # AUGMENT FLOW
        i = end
        while i != start:
            adj[i].append(parent[i])
            R[i] = parent[i]
            f[parent[i]][i] += 1
            f[i][parent[i]] -= 1
            i = parent[i]

        totalFlow += 1

    return totalFlow

print(maxFlow())
print(R)