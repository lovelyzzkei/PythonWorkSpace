import sys; read = sys.stdin.readline
from collections import deque

def bfs(y, x, wall):
    dq = deque([[y, x, wall]])
    dist = 1

    while dq:
        qlen = len(dq)
        visited = [[False for j in range(m)] for i in range(n)]
        visited[y][x] = True
        while qlen:
            cury, curx, cur_wall = dq.popleft()
            if cury == n-1 and curx == m-1:
                print(dist)
                return

            for i in range(4):
                ny = cury + dy[i]; nx = curx + dx[i]
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                    if _map[ny][nx]:
                        if cur_wall != 0: continue
                        else: wall = cur_wall + 1
                    visited[ny][nx] = True
                    dq.append([ny, nx, wall])
            qlen -= 1

        dist += 1

    print(-1)
    return

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, read().split())

_map = []
for i in range(n):
    input = read().strip()
    temp = []
    for j in range(m):
        temp.append(int(input[j]))
    _map.append(temp)

bfs(0, 0, _map[0][0])