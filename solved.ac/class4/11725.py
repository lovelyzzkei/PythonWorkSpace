import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
q = deque([])
parent = {i:i for i in range(1, n+1)}
for _ in range(n-1):
    a,b = map(int, read().split())
    if a == 1 or b == 1:
        parent[a] = 1; parent[b] = 1
    elif parent[a] != a:    parent[b] = a
    elif parent[b] != b:    parent[a] = b
    else:
        q.append([a, b])

# bfs
while q:
    a, b = q.popleft()
    if parent[a] != a:  parent[b] = a
    elif parent[b] != b:  parent[a] = b
    else:
        q.append([a, b])

print('\n'.join(str(x) for x in list(parent.values())[1:]))