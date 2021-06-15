import sys; read = sys.stdin.readline
from collections import deque

def bfs(start, node):
    q = deque([[start, 0]])
    visited = [False] * (n+1)
    visited[start] = True
    ret = []

    while q:
        findChild = False
        now, dist = q.popleft()
        for next, w in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append([next, dist + w])

        if not findChild:
            if node == 0:
                ret.append(now)
            else:
                ret.append(dist)

    return ret if node == 0 else max(ret)


n = int(read())
graph = {i:[] for i in range(1, n+1)}

for _ in range(n-1):
    u, v, w = map(int, read().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

# 트리의 맨 끝의 노드들 찾기
childNode = bfs(1, 0)

# 맨 끝 노드들부터 다른 모든 노드들까지의 거리 측정 (중복되는 노드들은 제외)
tree_dia = 0
for node in childNode:
    tree_dia = max(tree_dia, bfs(node, 1))

print(tree_dia)
