import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        # 그냥 루트를 x로 합침
        parent[y] = x
        nodeCount[x] += nodeCount[y]
        nodeCount[y] = 1

    ret.append(nodeCount[x])
    return

ret = []

for _ in range(int(read())):
    parent = {}
    nodeCount = {}
    for f in range(int(read())):
        a, b = read().split()
        if a not in parent:
            parent[a] = a
            nodeCount[a] = 1
        if b not in parent:
            parent[b] = b
            nodeCount[b] = 1

        union(a, b)

print('\n'.join(str(x) for x in ret))