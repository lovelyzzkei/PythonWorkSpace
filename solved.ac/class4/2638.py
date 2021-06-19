import sys; read = sys.stdin.readline
from collections import deque

def cheese(y, x):
    for i in range(4):
        ny = y + dy[i]; nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m and air[ny][nx]:
            _map[y][x] += 1


n, m = map(int, read().split())
_map = [list(map(int, read().split())) for j in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
time = 0

while any(any(x) for x in _map):
    air = [[False for j in range(m)] for i in range(n)]
    air[0][0] = True
    dq = deque([[0, 0]])

    # 외부 공기와 내부 공기 분리 (모눈종이의 맨 가장자리에는 치즈가 놓이지 않음)'
    while dq:
        cy, cx = dq.popleft()
        for i in range(4):
            ny = cy + dy[i]; nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if _map[ny][nx] == 0 and not air[ny][nx]:
                    air[ny][nx] = True
                    dq.append([ny, nx])   

    # 치즈 소멸 작업
    for i in range(n):
        for j in range(m):
            if _map[i][j]:
                cheese(i, j)
    
    # 전체 맵을 탐색하면서 3 이상의 수를 가지고 있는 치즈들 제거
    for i in range(n):
        for j in range(m):
            if _map[i][j]:
                if _map[i][j] >= 3:
                    _map[i][j] = 0
                else:
                    _map[i][j] = 1

    time += 1

print(time)