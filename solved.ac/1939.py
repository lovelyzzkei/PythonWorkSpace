import sys; read = sys.stdin.readline
from collections import deque

# BFS 풀이 -> 메모리 초과
# def bfs(x, y):
#     dq = deque([[x, INF]])
#     ans = 0

#     while dq:
#         cur, cur_weight = dq.popleft()
#         if cur == y:
#             ans = max(ans, cur_weight)
#             continue
        
#         for next in island[x]:
#             if not visited[cur][next[0]]:
#                 visited[cur][next[0]] = True; visited[next[0]][cur] = True
#                 dq.append([next[0], min(cur_weight, next[1])])

#     print(ans)
#     return

INF = 1_000_000_001
n, m = map(int, read().split())
island = {i:[] for i in range(1, n+1)}
visited = [[False for i in range(n+1)] for j in range(n+1)]

for _ in range(m):
    x, y, cost = map(int, read().split())
    island[x].append([y, cost])
    island[y].append([x, cost])


x, y = map(int, read().split())
bfs(x, y)