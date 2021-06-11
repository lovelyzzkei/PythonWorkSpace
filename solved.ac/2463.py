import sys; read = sys.stdin.readline
from collections import deque

# 시간 초과
def bfs(u, e):
    dq = deque([u])

    while dq:
        c = dq.popleft()
        for next, w in _map[c]:
            if not visited[next] and w > e:
                visited[c] = 1  # 고립되지 않았을 경우에만 현재 노드도 방문 처리
                visited[next] = 1
                dq.append(next)

    return


n, m = map(int, read().split())
edge = []
_map = {i:[] for i in range(1, n + 1)}

for _ in range(m):
    x, y, w = map(int, read().split())
    edge.append(w)
    _map[x].append([y, w])
    _map[y].append([x, w])

# 간선 가중치 순으로 정렬
edge.sort()
ans = 0
num = (n*(n-1))//2

for e in edge:
    ret = []
    visited = {i: 0 for i in range(1, n+1)}
    
    for i in range(1, n + 1):   # 최소 간선을 제거하고 탐색
        bfs(i, e)

    for i in range(1, n + 1):
        if not visited[i]:
            ret.append(i)  # 현재 간선을 제거했을 때 고립되는 노드 찾기

    for node in set(ret):
        if node != 0:
            num -= (n-node)
    print(e, visited, set(ret), num)   
    ans += e*(num*(num+1)//2)   # 고립되어 있는 노드의 간선의 개수를 제외하고 cost의 합 누적
    ans %= 1000000000

print(ans % 1000000000)
