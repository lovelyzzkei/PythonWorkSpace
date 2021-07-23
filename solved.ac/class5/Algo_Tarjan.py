import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, read().split())
graph = {i:[] for i in range(1, v+1)}
for _ in range(e):
    a, b = map(int, read().split())
    graph[a].append(b)

stack = []
low = [-1] * (v+1)
ids = [-1] * (v+1)
visited = [False] * (v+1)
idid = 0
result = []

def dfs(x):
    global idid
    ids[x] = idid
    low[x] = idid
    idid += 1
    visited[x] = True
    stack.append(x)

    for ne in graph[x]:
        if ids[ne] == -1:   # 아직 방문하지 않은 노드라면
            dfs(ne)
            low[x] = min(low[x], low[ne])
        elif visited[ne]:   # 지금 처리중인 노드
            low[x] = min(low[x], ids[ne])
    
    w = -1
    scc = []
    if low[x] == ids[x]:    # scc의 시작 노드라면
        while w != x:
            w = stack.pop()
            scc.append(w)
        result.append(scc)
  
for i in range(1, v+1):
    if ids[i] == -1:
        dfs(i)

print(result)