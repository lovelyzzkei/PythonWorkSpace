import sys; read = sys.stdin.readline
from collections import deque

def bfs(y1, x1, y2, x2):
    visited = {i:{j:False for j in range(n)} for i in range(n)}
    visited[y1][x1] = True
    q = deque([[y1+1, 0]])
    ret = graph[y1][x1]

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]; nx = cx + dx[i]
            if y1<=ny<=y2 and x1<=nx<=x2 and not visited[ny][nx]:
                visited[ny][nx] = True
                ret += graph[ny][nx]
                q.append([ny, nx])

    return ret

n, m = map(int, read().split())
graph = {i:{idx:value for idx, value in enumerate(map(int, read().split()))} for i in range(n)}
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ret = []
for _ in range(m): 
    y1, x1, y2, x2 = map(int, read().split())
    ret.append(bfs(y1-1, x1-1, y2-1, x2-1))

print('\n'.join(str(x) for x in ret))