import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
tree = {i:[] for i in range(1, n+1)}
dp = [0 for _ in range(n+1)]; dp[1] = 1

for t in range(n-1):
    u, v = map(int, read().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(root):
    q = deque([root])
    visited = {i:False for i in range(1, n+1)}
    visited[root] = True
    while q:
        node = q.popleft()
        for child in tree[node]:
            if not visited[child]:
                dp[child] = node
                visited[child] = True
                q.append(child)

dfs(1)
print('\n'.join(str(x) for x in dp[2:]))