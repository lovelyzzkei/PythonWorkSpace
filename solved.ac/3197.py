'''
백조의 호수
매일 물 공간과 접촉한 모든 빙판 공간은 녹음. 며칠이 지나야 백조들이 만날 수 있는가
1. 초기 상태에서 백조가 만날 수 있는지 확인 
2. 얼음을 녹임 -> 가장자리의 물들이 녹이는 거임 -> 얼음이 녹으면 가장자리 물이 됨 -> 중복 삭제 가능할듯
3. 백조가 만날 수 있는지 확인 -> 시간 단축 필요
3-1. BFS로 구현하면 시간초과가 뜸
4. 2~3을 만날 때까지 확인
'''

import sys; read = sys.stdin.readline
from collections import deque

r, c = map(int, read().split())
lake = []; t = []; edge = deque([])
melted = [[False for j in range(c)] for i in range(r)]
for i in range(r):
    tmp = []; input = read().strip()
    for j in range(c):
        if input[j] == 'X':
            tmp.append(1)
        else:
            tmp.append(0)
            if input[j] == '.':
                edge.append([i, j])
                melted[i][j] = True
            else:
                t.append([i, j])
    lake.append(tmp)

# for item in lake:
#     print(item)
# 1. 초기 상태에서 백조가 만날 수 있는지 확인
def inMap(y, x):
    return 0<=y<r and 0<=x<c

def bfs():
    q = deque([t[0]])
    visited = [[False for j in range(c)] for i in range(r)]
    for y, x in q:
        visited[y][x] = True
    while q:
        cy, cx = q.popleft()
        if [cy, cx] == t[1]:
            return True
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx) and not visited[ny][nx] and lake[ny][nx] == 0:
                visited[ny][nx] = True
                q.append([ny, nx])

    return False

def melt():
    qlen = len(edge)
    find1 = False; find2 = False
    for tc in range(qlen):
        cy, cx = edge.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx) and not melted[ny][nx]:
                if [ny, nx] == t[0]:
                    find1 = True
                elif [ny, nx] == t[1]:
                    find2 = True 
                elif lake[ny][nx] == 1:
                    lake[ny][nx] = 0
                    melted[ny][nx] = True
                    edge.append([ny, nx])
        if find1 and find2:
            return True
    return False

date = 0
while True:
    # 얼음 녹이며 만나는지 확인
    if melt():
        break
    date += 1
print(date)
