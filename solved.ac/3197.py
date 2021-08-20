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
parent = [i for i in range(r*c)]
for i in range(r):
    tmp = []; input = read().strip()
    for j in range(c):
        if input[j] == 'X':
            tmp.append(1)
        else:
            tmp.append(0)
            edge.append([i, j])
            if input[j] == 'L':
                t.append([i, j])
    lake.append(tmp)

# for item in lake:
#     print(item)
# 1. 초기 상태에서 백조가 만날 수 있는지 확인
def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a); b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def inMap(y, x):
    return 0<=y<r and 0<=x<c


def bfs():
    q = deque(t.copy())
    visited = [[False for j in range(c)] for i in range(r)]
    for y, x in q:
        visited[y][x] = True
    while q:
        cy, cx = q.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx) and not visited[ny][nx] and lake[ny][nx] == 0:
                parent[ny*c+nx] = parent[cy*c+cx]
                visited[ny][nx] = True
                q.append([ny, nx])

def melt():
    qlen = len(edge)
    for tc in range(qlen):
        cy, cx = edge.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx) and lake[ny][nx] == 1:
                parent[ny*c+nx] = parent[cy*c+cx]
                lake[ny][nx] = 0
                edge.append([ny, nx])

def merge():
    qlen = len(edge)
    for tc in range(qlen):
        cy, cx = edge[tc]
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny=cy+dy; nx=cx+dx
            if inMap(ny, nx) and lake[ny][nx] == 0 and parent[ny*c+nx] != parent[cy*c+cx]:
                union(ny*c+nx, cy*c+cx)

date = 0
bfs()
l1 = t[0][0]*c+t[0][1]
l2 = t[1][0]*c+t[1][1]

while True:
    # 얼음 녹이기
    melt()
    date += 1
    merge()
    if find(l1) == find(l2):
        break

print(date)
