import sys; read = sys.stdin.readline
from itertools import combinations
from collections import deque

n, m = map(int, read().split())

lab = [list(map(int, read().split())) for i in range(n)]
coor = []; virus = []; walls = []

# 바이러스와 빈칸 찾기
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i, j))
        if lab[i][j] == 1:
            walls.append((i, j))
        if lab[i][j] == 0:
            coor.append((i, j))

# 빈칸의 좌표를 조합하여 3개의 벽을 세울 수 있는 좌표를 모두 구해둠
new_walls = list(combinations(coor, 3))
# print(len(walls))

def bfs(new_wall_num):
    q = deque(virus[:])
    visited = [[False for _ in range(m)] for __ in range(n)]
    for y, x in virus:
        visited[y][x] = True
    for y, x in new_walls[new_wall_num]:
        visited[y][x] = True
    for y, x in walls:
        visited[y][x] = True
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([ny, nx])
    
    safe = 0
    # 안전 구역의 크기를 구하여 return
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                safe += 1
    return safe

ret = []
for num in range(len(new_walls)):
    ret.append(bfs(num))

# print(ret)
print(max(ret))
