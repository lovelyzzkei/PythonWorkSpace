import sys; read = sys.stdin.readline
from collections import deque

ret = []
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y, tar_x, tar_y):
    visited = [[False for j in range(l)] for i in range(l)]
    dist = 0

    dq = deque([[y, x]])
    while dq:
        qlen = len(dq)
        while qlen:
            cur_y, cur_x = dq.popleft()

            if cur_y == tar_y and cur_x == tar_x:
                ret.append(dist)
                return
            
            for i in range(8):
                ny = cur_y + dy[i]; nx = cur_x + dx[i]
                if 0 <= ny < l and 0 <= nx < l and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dq.append([ny, nx])
            qlen -= 1
        dist += 1

for _ in range(int(read())):
    l = int(read())

    x, y = map(int, read().split())
    tar_x, tar_y = map(int, read().split())
    bfs(x, y, tar_x, tar_y)

print('\n'.join(str(x) for x in ret))