import sys; read = sys.stdin.readline
from collections import deque

r, c = map(int, read().split())
lake= []; start = []    # 백조의 위치 저장
for i in range(r):
    row = read().strip(); row_list = []
    for item in row:
        if item == ".": row_list.append(-1)
        elif item == "X":   row_list.append(1)
        else:
            start.append([i, row.index(item)])
            row_list.append(2)
    lake.append(row_list)

# for item in lake:
#     print(item)

parents = [[[j, i] for i in range(c)] for j in range(r)]
edge = deque([])
canGo = False

def inMap(y, x):
    return 0<=y<r and 0<=x<c

def bfs(c1, c2):
    global canGo
    q = deque([c1.copy()])
    visited = [[False for i in range(c)] for j in range(r)]
    visited[c1[0]][c1[1]] = True

    while q:
        cy, cx = q.popleft()
        if parents[cy][cx] == c2[:]:
            canGo = True
            return
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny = cy + dy; nx = cx + dx
            isEdge = True
            if inMap(ny, nx) and not visited[ny][nx]:
                if lake[ny][nx] == -1:
                    parents[ny][nx] = c1.copy()
                    visited[ny][nx] = True
                    isEdge = False
                    q.append([ny, nx])
        # 각 영역에서 가장 가장자리에 존재하는 물들을 저장해놓음
        if isEdge:
            edge.append([cy, cx, c1])

date = 0
# 각 백조와 맞닿아 있는 물을 해당 백조에게 귀속시킴
bfs(start[0], start[1])
bfs(start[1], start[0])
if not canGo:
    while True:
        # 얼음 녹이기 -> 모든 물에 대하여 돌리는게 맞는듯...
        qlen = len(edge)
        for tc in range(qlen):
            y, x, p = edge.popleft()
            lake[y][x] = -1
            parents[y][x] = p
            for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                ny = y + dy; nx = x + dx
                if inMap(ny, nx):
                    if parents[ny][nx] != [ny, nx] and parents[ny][nx] != p: # 해당 물이 어딘가에 귀속되어있음 -> 연결되어있음
                        canGo = True
                        break
                    if lake[ny][nx] == 1:
                        edge.append([ny, nx, parents[y][x]])
            
            # print()
            # for item in parents:
            #     print(item)
        
        if canGo:
            break
        date += 1

print(date)
