import sys;read = sys.stdin.readline
import heapq

n, m = map(int, read().split())
inDegree = {i:0 for i in range(1, n+1)}
tree = {i:[] for i in range(1, n+1)}

for tc in range(m):
    u, v = map(int, read().split())
    inDegree[v] += 1
    tree[u].append(v)

def tp_sort():
    q = []
    for i in range(1, n+1):
        if inDegree[i] == 0:
            heapq.heappush(q, i)

    ans = []
    while q:
        now = heapq.heappop(q)
        ans.append(now)
        for child in tree[now]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                heapq.heappush(q, child)

    print(' '.join(str(x) for x in ans))

tp_sort()