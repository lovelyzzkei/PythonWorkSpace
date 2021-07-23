import sys; read = sys.stdin.readline
from collections import deque

n, L = map(int, read().split())
inDegree = {i:0 for i in range(n+2)}
tree = {i:[] for i in range(1, n+1)}
time = {i:0 for i in range(1, n+1)}
ice = [0] * (100002)

q = deque([])

for i in range(1, n+1):
    ice[i] = int(read())

for i in range(1, n+1):
    if ice[i-1] < ice[i]:
        inDegree[i-1] += 1
        tree[i].append(i-1)
    if ice[i+1] < ice[i]:
        inDegree[i+1] += 1
        tree[i].append(i+1)
    if len(tree[i]) == 2:
        q.append(i)
  
def tp_sort():
    cul_time = {i:[0] for i in range(n+2)}

    while q:
        now = q.popleft()
        if now != 0 and now != n+1:
            time[now] += L-ice[now] + max(cul_time[now])
            for child in tree[now]:
                inDegree[child] -= 1
                cul_time[child].append(time[now])
                if inDegree[child] == 0:
                    q.append(child)

tp_sort()
print(max(time.values()))