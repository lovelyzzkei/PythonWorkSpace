import sys; read = sys.stdin.readline
from collections import deque

m, n = map(int, read().split())
maze = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = int(1e9)

def bfs(y, x):
    dq = deque([[y, x, 0]])
    d = [[INF] * m for i in range(n)]
    d[y][x] = 0

    while dq:
        cy, cx, cwall = dq.popleft()
        if d[cy][cx] < cwall:
            continue
        
        for i in range(4):
            ny=cy+dy[i]; nx=cx+dx[i]
            if 0<=ny<n and 0<=nx<m:
                nwall = cwall + maze[ny][nx]
                if nwall < d[ny][nx]:
                    d[ny][nx] = nwall
                    dq.append([ny, nx, nwall])

    return d[n-1][m-1]


for i in range(n):
    temp = []
    input = read().strip()
    for j in range(m):
        temp.append(int(input[j]))
    maze.append(temp)


print(bfs(0, 0))