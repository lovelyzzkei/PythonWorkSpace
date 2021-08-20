import sys; read = sys.stdin.readline
from collections import deque

r, c = map(int, read().split())
cave = []
for i in range(r):
    tmp = []; input = read().strip()
    for j in range(c):
        if input[j] == '.':
            tmp.append(0)
        else:
            tmp.append(1)
    cave.append(tmp)

def breakMineral(rod_now, turn):
    h = r - rod_now
    if turn % 2 == 0:
        i = 0
        while i < c:
            if cave[h][i] == 1:    # 미네랄과 만나면 부수고 스탑
                cave[h][i] = 0
                return True
            i += 1
    else:
        i = c-1
        while i > -1:
            if cave[h][i] == 1:
                cave[h][i] = 0
                return True
            i -= 1

    return False

def inMap(y, x):
    return 0<=y<r and 0<=x<c

def bfs(y, x):
    q = deque([[y, x]])
    visited[y][x] = True
    onGround = False
    while q:
        cy, cx = q.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx) and not visited[ny][nx] and cave[ny][nx] == 1:
                if parent[ny*c+nx] != parent[cy*c+cx]:
                    parent[ny*c+nx] = parent[cy*c+cx]
                    visited[ny][nx] = True
                    if ny == r-1:
                        onGround = True
                    q.append([ny, nx])

    return [parent[y*c+x], onGround]

def sumCluster(cp):
    height = []; 
    for j in range(c):  #각 열에서
        n = r
        for i in range(r-1, -1, -1):    # 가장 밑에 있는 미네랄 탐색
            if cave[i][j] == 1:
                if parent[i*c+j] == cp:
                    height.append(n-i-1)
                else:
                    n = i
    h = min(height)

    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            if parent[i*c+j] == cp:
                cave[i+h][j] = 1
                cave[i][j] = 0



# 턴이 짝수: 왼->오 / 홀수: 오->왼
n = int(read())
rod = list(map(int, read().split()))
for turn in range(n):
    rod_now = rod[turn]
    if breakMineral(rod_now, turn):
        # 미네랄이 분리되었는지 확인
        parent = [i for i in range(r*c)]
        visited = [[False for j in range(c)] for i in range(r)]
        cluster = deque([])
        for i in range(r):
            for j in range(c):
                if cave[i][j] == 1 and not visited[i][j]:
                    cluster.append(bfs(i, j))
        # 각각의 클러스터가 바닥에 붙어있는지 확인하고 합치는 작업 진행
        while cluster:
            cp, onGround = cluster.popleft()
            if not onGround:
                sumCluster(cp)
    

ans = []
for i in range(r):
    tmp = ''
    for j in range(c):
        if cave[i][j] == 0:
            tmp += '.'
        else:
            tmp += 'x'
    ans.append(tmp)
print('\n'.join(x for x in ans))