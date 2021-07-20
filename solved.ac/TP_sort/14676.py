import sys; read = sys.stdin.readline
from collections import deque

n, m, k = map(int, read().split())
inDegree = {i:0 for i in range(1, n+1)}
tree = {i:[] for i in range(1, n+1)}
count = {i:0 for i in range(1, n+1)}
visited = {i:False for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, read().split())
    inDegree[v] += 1
    tree[u].append(v)

useCheat = False
for tc in range(k):
    order, build = map(int, read().split())
    if order == 1:      # 건물 건설
        if inDegree[build] == 0:    # 진입 차수가 0, 이전의 건물들이 건설되어 있어야만 건설 가능
            count[build] += 1
            if not visited[build]:
                visited[build] = True
                for child in tree[build]:
                    inDegree[child] -= 1
        else:
            useCheat = True
            continue

    if order == 2:      # 건물 파괴 1. 건물이 건설되어 있어야만 2. 이전의 건물들이 건설 되어있어야만
        if count[build] > 0:
            count[build] -= 1
            if count[build] == 0:   # 해당 건물이 모두 파괴되었으면
                visited[build] = False
                for child in tree[build]:   # 다음 건물을 건설하기 이전에 다시 건설할 필요가 존재
                    inDegree[child] += 1

        else:
            useCheat = True
            continue

if useCheat:
    print("Lier!")
else:
    print("King-God-Emperor")

