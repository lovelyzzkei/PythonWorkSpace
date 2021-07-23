import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
m = int(read())
inDegree = {i:0 for i in range(1, n+1)}
graph = {i:[] for i in range(1, n+1)}
path = {i:[] for i in range(1, n+1)}
d = [0] * (n+1)    # 최장거리, 그 거리까지의 경로

for tc in range(m):
    p, q, r = map(int, read().split())
    graph[p].append([q, r])
    inDegree[q] += 1

# print(inDegree)
# print(graph)

def tp_sort():
    q = deque([1])  # 1에서 시작
    path[1].append(1)

    while q:
        now = q.popleft()
        if now == 1 and len(path[1]) != 1:  # 다시 1로 돌아왔을 경우 최댓값이 갱신될떄까지 계속 돌림
            inDegree[1] += 1    # 1로 돌아오는 경로를 또 사용할 수 있으므로 1의 INDEGREE값을 복구해놓음
            continue
        for child, w in graph[now]:
            inDegree[child] -= 1
            if d[now] + w > d[child]:
                d[child] = d[now] + w
                path[child] = path[now].copy()
                path[child].append(child)
            if inDegree[child] == 0:
                q.append(child)

tp_sort()
print(d[1])
print(' '.join(str(x) for x in path[1]))