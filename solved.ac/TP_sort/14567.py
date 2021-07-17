import sys; read = sys.stdin.readline
from collections import deque
n, m = map(int, read().split())
in_degree = {i:0 for i in range(1, n+1)}
major = {i:[] for i in range(1, n+1)}
time = {i:1 for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, read().split())
    in_degree[v] += 1
    major[u].append(v)

def tp_sort():
    q = deque([])
    cul_time = [[0] for _ in range(n+1)]
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        time[now] += max(cul_time[now])
        for next_major in major[now]:
            in_degree[next_major] -= 1
            cul_time[next_major].append(time[now])
            if in_degree[next_major] == 0:
                q.append(next_major)
    
    print(' '.join(str(x) for x in list(time.values())))

tp_sort()