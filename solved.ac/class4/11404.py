import sys; read = sys.stdin.readline

INF = int(1e8)
n = int(read())
m = int(read())
t = [[INF for j in range(n+1)] for i in range(n+1)]

def floyd():
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if t[start][end] > t[start][mid] + t[mid][end]:
                    t[start][end] = t[start][mid] + t[mid][end]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if t[i][j] == INF:
                print(0, end=" ")
            else:
                print(t[i][j], end=" ")
        print()

    
for _ in range(m):
    u, v, w = map(int, read().split())
    t[u][v] = min(t[u][v], w)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: t[i][j] = 0

floyd()