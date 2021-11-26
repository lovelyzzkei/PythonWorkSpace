import sys; read = sys.stdin.readline
from collections import deque

MAX_N = 201
INF = sys.maxsize

c = [[0 for i in range(MAX_N)] for j in range(MAX_N)]
f = [[0 for i in range(MAX_N)] for j in range(MAX_N)]
w = [[0 for i in range(MAX_N)] for j in range(MAX_N)]

n, m = map(int, read().split())

a = {i:[] for i in range(n+m+2)}
v = [INF for i in range(n+m+2)]

def maxFlow(block):
    totalFlow = 0
    s = 0; t = n + m + 1

    while True:
        parent = [-1 for i in range(n+m+2)]
        parent[0] = 0
        q = deque([s])
        
        # BFS
        while len(q) != 0 and parent[t] == -1:
            x = q.pop()

            for y in a[x]:
                if c[x][y] - f[x][y] > 0 and parent[y] == -1:
                    q.append(y)
                    parent[y] = x
        
        if parent[t] == -1:
            break

        # MCMF
        flow = INF
        i = t
        while i != s:
            flow = min(flow, c[parent[i]][i] - f[parent[i]][i])
            i = parent[i]
            print(parent, i, flow)
        
        while i != s:
            a[parent[i]].append(i)
            f[parent[i]][i] += flow
            f[i][parent[i]] -= flow
            i = parent[i]
        
        y = parent[t]
        x = parent[y]
        print(f[x][y], c[x][y])
        totalFlow += flow * w[x][y]
        
        sum_flow = 0
        for i in range(m):
            sum_flow += f[m+i+1][m+n+1]
        print(sum_flow)
        if sum_flow == block:
            break

    return totalFlow




A = list(map(int, read().split()))
B = list(map(int, read().split()))

# 사람 - sink 연결
for i in range(n):
    a[m+i+1].append(n+m+1)  
    c[m+i+1][n+m+1] = A[i]

# source - 서점
for i in range(m):
    a[0].append(i+1)
    c[0][i+1] = B[i]

# 서점 - 사람 연결
for i in range(m):
    tmp = list(map(int, read().split()))
    for j in range(n):
        a[i+1].append(m+i+j)
        c[i+1][m+j+1] = sum(A)
        w[i+1][m+j+1] = tmp[j]


print(a)
print(maxFlow(sum(A)))