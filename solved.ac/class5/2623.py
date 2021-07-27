import sys; read= sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
inDegree = {i:0 for i in range(1, n+1)}
tree = {i:[] for i in range(1, n+1)}
visited = {i:False for i in range(1, n+1)}

for tc in range(m):
    singers = list(map(int, read().split()))
    num_singers = singers[0]
    for i in range(1, num_singers):
        u, v = singers[i], singers[i+1]
        inDegree[v] += 1
        tree[u].append(v)
# print(tree)
# print(inDegree)

def tp_sort():
    q = deque([])
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
            visited[i] = True

    ans = []
    while q:
        now = q.popleft()
        ans.append(now)
        for child in tree[now]:
            if visited[child]:  # 사이클이 존재
                return [0]
            inDegree[child] -= 1
            if inDegree[child] == 0:
                q.append(child)
                visited[child] = True
    
    return ans

ret = tp_sort()
if len(ret) != n:   # 사이클이 존재할 경우 진입차수가 0인 것들이 존재할 수 없음
    print(0)
else:
    print('\n'.join(str(x) for x in ret))
