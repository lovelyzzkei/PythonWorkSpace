import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


n, m = map(int, read().split())

parent = {i:i for i in range(n+1)}
rank = {i:1 for i in range(n+1)}
ret = []

for i in range(m):
    oper, a, b = map(int, read().split())

    if oper == 0:
        union(a, b)
    
    if oper == 1:
        a = find(a)
        b = find(b)
        ret.append("YES" if a == b else "NO")

print('\n'.join(x for x in ret))