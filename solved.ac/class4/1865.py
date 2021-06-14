import sys; read = sys.stdin.readline
from collections import deque

def spfa(start):
    d = [INF] * (n+1)
    d[start] = 0
    cycle = [0] * (n+1)

    dq = deque([start])

    inQueue = [False] * (n+1)
    inQueue[start] = True

    while dq:
        now = dq.popleft()
        inQueue[now] = False

        if now == start and d[now] < 0:
            return True

        for nextNode in _map[now]:
            v, w = nextNode
            if d[now] + w < d[v]:
                d[v] = d[now] + w

                if not inQueue[v]:
                    cycle[v] += 1
                    if cycle[v] >= n:   # 음수 사이클이 존재하는 경우
                        return False
                    dq.append(v)
                    inQueue[v] == True



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
        if spfa(i):
            isBack = True
            break

    if isBack: ret.append('YES')
    else: ret.append('NO')

print('\n'.join(ret))