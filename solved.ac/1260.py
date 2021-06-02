import sys; read=sys.stdin.readline
from collections import deque

graph = [ deque([]) for i in range(1010) ]
result = []

def bfs(start_node):    
    visited = {}    # 더 빠르게 방문여부 탐색
    q = deque([start_node])

    while q:
        node = q.popleft()
        if node not in visited:
            visited[node] = True   
            temp = []    
            for nextNode in graph[node]:
                temp.append(nextNode)
            q += deque(sorted(temp))

    result.append(' '.join(str(x) for x in visited.keys()))


def dfs(start_node):
    visited = {}
    q = deque([start_node])

    while q:
        node = q.pop()
        if node not in visited:
            visited[node] = True
            temp = []
            for nextNode in graph[node]:
                temp.append(nextNode)
            q += deque(sorted(temp, reverse=True))
    
    result.append(' '.join(str(x) for x in visited.keys()))

n, m, start_node = map(int, read().split())

for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

graph = {idx:item for idx, item in enumerate(graph)}

dfs(start_node)
bfs(start_node)

print('\n'.join(result))