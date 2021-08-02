import sys; read = sys.stdin.readline
INF = int(1e5)

n, m = map(int, read().split())
graph = {i:[] for i in range(1, n+1)}
d = [[INF for i in range(n+1)] for j in range(n+1)]
ret = [['-' for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    u, v, w = map(int, read().split())
    d[u][v] = d[v][u] = w
    ret[u][v] = v
    ret[v][u] = u

def bellmanFord(s, e):
    for i in range(1, n+1):
        d[i][i] = 0
        
    for mid in range(s, e):
        for start in range(s, e):
            if start != mid:
                for end in range(s, e):
                    if d[start][mid] + d[mid][end] < d[start][end]:
                        d[start][end] = d[start][mid] + d[mid][end]
                        ret[start][end] = ret[start][mid]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(ret[i][j], end=" ")
        print()

bellmanFord(1, n+1)