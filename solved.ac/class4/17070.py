import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
wall = {i: {idx: v for idx, v in enumerate(list(map(int, read().split())))} for i in range(n)}
# 가로:1, 세로:2, 대각:3 으로 설정하여 각 방향마다 [dy, dx, 다음 방향]을 저장해놓음
mode = {1:[[0,1,1],[1,1,3]], 2:[[1,0,2],[1,1,3]], 3:[[0,1,1],[1,0,2],[1,1,3]]}  

# 이동하려는 좌표가 집 안에 있는지 + 벽이 있는지
def possible(cy, cx, dy, dx):
    if cy+dy<0 or cy+dy>=n or cx+dx<0 or cx+dx>=n:
        return False
    return not wall[cy+dy][cx] and not wall[cy][cx+dx] and not wall[cy+dy][cx+dx]

# BFS로 가능한 가짓수 탐색. 이때 방문처리는 x
def bfs(y, x):
    q = deque([[y, x, 1]])
    ret = 0

    while q:
        cy, cx, m = q.popleft()
        if cy == n-1 and cx == n-1:
            ret += 1
            continue
        for dir in mode[m]:
            dy, dx, next_mode = dir
            if possible(cy, cx, dy, dx):
                ny=cy+dy; nx=cx+dx
                q.append([ny, nx, next_mode])
    
    return ret
print(bfs(0, 1))