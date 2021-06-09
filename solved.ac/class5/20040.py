import sys; read = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y, i):
    global isCycle, ans

    x = find(x); y = find(y)
    if x == y:
        isCycle = True
        ans = i
        return
    
    # 높이가 더 낮은 트리를 높은 트리에 합침
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


isCycle = False         # 사이클 형성을 알기 위한 플래그

n, m = map(int, read().split())

parent = {i:i for i in range(n)}
rank = {i:0 for i in range(n)}  # 트리의 높이
ans = 0

for i in range(1, m+1):
    x, y = map(int, read().split())
    if isCycle:
        continue
    union(x, y, i)

print(ans)