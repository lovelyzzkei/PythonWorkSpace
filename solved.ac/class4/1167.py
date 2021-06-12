import sys; read = sys.stdin.readline
from collections import deque

def find(x):
    if parent[x][0] == x:
        return x
    parent[x][0] = find(parent[x][0])
    return parent[x][0]

def union(x, y):
    x = find(x); y = find(y)

    if x == y: return
    if parent[x][1] < parent[y][1]:
        parent[x][0] = y
    else:
        parent[y][0] = x
        if parent[x][1] == parent[y][1]:
            parent[x][1] += 1

def dfs(root, child, height):
    dq = deque([[child, height]])
    visited = {i:0 for i in range(1, v+1)}
    visited[root] = 1; visited[child] = 1
    max_height = 0

    while dq:
        hasChild = False
        cur, cur_h = dq.pop()

        for child in tree[cur]:
            if not visited[child[0]]:
                visited[child[0]] = 1
                dq.append([child[0], cur_h + child[1]])
                hasChild = True
        if not hasChild:
            max_height = max(max_height, cur_h)  # 현재 가지에서 가장 긴 길이

    return max_height       


v = int(read())

tree = {i:[] for i in range(1, v+1)}
parent = {i:[i, 0] for i in range(1, v+1)}

for _ in range(v):
    edge = list(map(int, read().split()))[:-1]
    node = edge[0]
    for i in range(len(edge) // 2):
        union(node, edge[i*2+1])        # 루트 노드를 찾기 위한 union-find
        tree[node].append(edge[i*2+1:(i+1)*2+1])

root = parent[1][0]

ret = []
for child in tree[root]:
    ret.append(dfs(root, child[0], child[1]))

ret.sort(reverse=True)
if len(ret) == 1:   print(ret[0])
else:   print(ret[0] + ret[1])