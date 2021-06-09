import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x); y = find(y)

    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


n = int(read())
m = int(read())

parent = {i:i for i in range(1, n+1)}
rank = {i:0 for i in range(1, n+1)}

for _ in range(m):
    x, y = map(int, read().split())
    for i in range(x, y):
        union(i, i+1)

for i in range(1, n+1):
    find(i)

print(len(set(parent.values())))