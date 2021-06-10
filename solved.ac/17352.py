import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x); y = find(y)

    if rank[x] < rank[y]:
        parent[x] = y

    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

n = int(read())
parent = {i:i for i in range(1, n + 1)}
rank = {i:0 for i in range(1, n + 1)}

for i in range(n-2):
    x, y = map(int, read().split())
    union(x, y)

for i in range(1, n + 1):
    find(i)

print(' '.join(str(x) for x in set(parent.values())))