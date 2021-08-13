import sys; read = sys.stdin.readline
from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


r, c = map(int, read().split())
lake= []; bird = []; num_bird = 1    # 백조의 위치 저장
q = deque([])
for i in range(r):
    row = read().strip(); row_list = []
    for j in range(c):
        item = row[j]
        if item == ".": 
            row_list.append(-1)
            q.append([i, j])
        elif item == "X":   row_list.append(0)
        else:
            bird.append([i, j, num_bird])
            row_list.append(num_bird)
            num_bird += 1   # 두 백조의 id를 다르게 저장
    lake.append(row_list)

parents = [[-1 for j in range(c)] for i in range(r)]
visited = [[False for j in range(c)] for i in range(r)]

def inMap(y, x):
    return 0<=y<r and 0<=x<c

def bfs():
    dq = deque(bird.copy())
    for y, x, num in dq:
        visited[y][x] = True
    
    while dq:
        cy, cx, c_parent = dq.popleft()
        for i in range(4):
            ny=cy+dy[i]; nx=cx+dx[i]
            if inMap(ny, nx) and not visited[ny][nx]:
                if lake[ny][nx] == -1:
                    visited[ny][nx] = True
                    parents[ny][nx] = c_parent
                    dq.append([ny, nx, c_parent])


for y, x, _id in bird:
    parents[y][x] = _id
bfs()

# for item in parents:
#     print(item)

findBird1 = False; findBird2 = False; date = 0
while not findBird1 or not findBird2:
    qlen = len(q)
    for tc in range(qlen):
        y, x = q.popleft()
        if parents[y][x] == 1: findBird1 = True
        if parents[y][x] == 2: findBird2 = True
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if inMap(ny, nx) and lake[ny][nx] == 0:
                lake[ny][nx] = -1
                if parents[y][x] != -1:
                    parents[ny][nx] = parents[y][x]
                q.append([ny, nx])

    date += 1

print(date)
