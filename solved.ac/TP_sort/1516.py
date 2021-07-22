import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
inDegree = {i:0 for i in range(1, n+1)}
tree = {i:[] for i in range(1, n+1)}
time = {i:0 for i in range(1, n+1)}

for build in range(1, n+1):
    input = list(map(int, read().split()))[:-1]
    time[build] = input[0]
    for parent in input[1:]:
        inDegree[build] += 1
        tree[parent].append(build)

# print(tree)
# print(inDegree)
# print(time)

def tp_sort():
    q = deque([])
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    cul_time = {i:[0] for i in range(1, n+1)}
    while q:
        now = q.popleft()
        time[now] += max(cul_time[now])

        for child in tree[now]:
            inDegree[child] -= 1
            cul_time[child].append(time[now])
            if inDegree[child] == 0:
                q.append(child)

tp_sort()
print('\n'.join(str(x) for x in time.values()))