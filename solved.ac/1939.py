import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y, cost):
    px = find(x); py = find(y)

    # 다리가 양방향이므로 x에서 y로 가는 길에는 두 가지 방법이 존재한다
    # 1. x에서 자신의 부모를 거쳐 y로 가는 길
    # 2. y에서 자신의 부모를 거쳐 x로 가는 길
    x_y = min(weight[x][px], weight[px][y])     
    y_x = min(weight[y][py], weight[py][x])
    weight[x][y] = max(x_y, y_x, cost)
    weight[y][x] = weight[x][y]

    # 경로 압축을 위한 union-by-rank
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

n, m = map(int, read().split())

parent = {i:i for i in range(1, n+1)}
rank = {i:0 for i in range(1, n+1)}
weight = [[0] * (n+1) for i in range(n+1)]

for t in range(m):
    x, y, cost = map(int, read().split())
    union(x, y, cost)

x, y = map(int, read().split())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(weight[i][j], end=" ")
    print()

print(weight[x][y])