import sys; read = sys.stdin.readline
from collections import deque

n, m, c = map(int, read().split())
tree = {i:[] for i in range(1, n+1)}
inDegree = {i:0 for i in range(1, n+1)}
limit = {i+1:v for i, v in enumerate(list(map(int, read().split())))}
for _ in range(c):
    a, b, x = map(int, read().split())
    tree[a].append([b, x])
    inDegree[b] += 1

# print(tree)
# print(inDegree)
# print(time)

def tp_sort():
    q = deque([])
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
    
    time = {i:0 for i in range(1, n+1)}
    candidate = {i:[0] for i in range(1, n+1)}
    while q:
        now = q.popleft()
        if max(candidate[now]) < limit[now]:
            time[now] = limit[now]
        else:
            time[now] = max(candidate[now])

        for child, w in tree[now]:
            inDegree[child] -= 1
            candidate[child].append(time[now] + w)
            if inDegree[child] == 0:
                q.append(child)
        # print(candidate)

    print('\n'.join(str(x) for x in time.values()))

tp_sort()