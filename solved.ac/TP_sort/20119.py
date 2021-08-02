import sys; read = sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
inDegree = {i:[] for i in range(1, n+1)}
recipe = {i:[] for i in range(1, n+1)}
for _ in range(m):
    tc = list(map(int, read().split()))
    k = tc[0]; r = tc[-1]
    for i in range(1, k+1):
        recipe[tc[i]].append(r)
    inDegree[r].append({i:False for i in tc[1:-1]})

l = int(read())
now = list(map(int, read().split()))

def tp_sort():
    ret = []
    q = deque(now.copy())
    visited = {i:False for i in range(1, n+1)}
    for i in q:
        ret.append(i)
        visited[i] = True

    while q:
        potion = q.popleft()
        for nxt in recipe[potion]:
            if not visited[nxt]:
                for r in inDegree[nxt]:
                    r[potion] = True

                    if all(r.values()):
                        visited[nxt] = True
                        ret.append(nxt)
                        q.append(nxt)

    print(len(ret))
    print(' '.join(str(x) for x in sorted(ret)))

tp_sort()