import sys; read = sys.stdin.readline
from collections import deque

def bf(start):
    d = [INF] * (n+1)
    d[start] = 0
    inqueue = [False] * (n+1)

    dq = deque([start])
    inqueue[start] = True

    while dq:
        u = dq.popleft()
        inqueue[u] = False

        for i in range(len(_map[u])):
            v, w = _map[u][i]

            if d[u] + w < d[v]:
                d[v] = d[u] + w

                if inqueue[v] == False:
                    dq.append(v)
                    inqueue[v] = True

    return True if d[start] < 0 else False
    # for _ in range(n-1):
    #     for node in _map:
    #         for neighbor in _map[node]:
    #             v, w = neighbor
    #             if d[node] != INF and d[node] + w < d[v]:
    #                 d[v] = d[node] + w

    # 음수 사이클 확인 
    # for node in _map:
    #     for neighbor in _map[node]:
    #         v, w = neighbor
    #         if d[node] != INF and d[node] + w < d[v]:


tc = int(read())
ret = []
INF = int(1e9)

for t in range(tc):
    n, m, w = map(int, read().split())
    _map = {i:[] for i in range(1, n+1)}
    isBack = False

    for _ in range(m):
        s, e, t = map(int, read().split())
        _map[s].append([e, t])
        _map[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int, read().split())
        _map[s].append([e, -t])

    for i in range(1, n+1):
        if bf(i):
            isBack = True
            break

    if isBack: ret.append('YES')
    else: ret.append('NO')

print('\n'.join(ret))