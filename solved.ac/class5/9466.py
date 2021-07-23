import sys; read = sys.stdin.readline
sys.setrecursionlimit(10**4)

t = int(read())
ret = []
for _ in range(t):
    v = int(read())
    graph = {i+1:[v] for i, v in enumerate(list(map(int, read().split())))}
    stack = []
    low = [-1] * (v+1)
    ids = [-1] * (v+1)
    visited = [False] * (v+1)
    idid = 0
    result = []
    len_scc = 0

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
    len_scc = sum(len(s) for s in result)
    for s in result:
        if len(s) == 1 and graph[s[0]][0] != s[0]:
            len_scc -= 1
    ret.append(v-len_scc)
    # print(ids)
    # print(low)
    # print(result)
    
print('\n'.join(str(x) for x in ret))