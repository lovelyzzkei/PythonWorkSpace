import sys; read = sys.stdin.readline
from collections import deque

def binary_search():
    global max_weight
    res = 1
    min = 1
    while min <= max_weight:
        print(max_weight)
        mid = (min + max_weight) // 2
        # 만약에 현재 섬에서 최소 중량 제한과 최대 중량 제한 사이의 중량 제한을 가진 다리를 건널 수 있다면
        # 두 섬 사이를 이동할 수 있는 중량의 최대는 최소한 중간값보다 크거나 같게 된다.
        # 따라서 현재 섬에서 탐색을 하여 만약에 이동이 가능하면 중간값을 최솟값으로 잡고 다시 탐색을 시작하고
        # 그렇지 않다면 중간값을 최댓값으로 잡고 다시 탐색을 시작하여
        # 최종적으로 두 섬을 이동할 수 있는 중량의 최댓값을 구하게 된다.
        if bfs(s, e, mid):
            res = max(res, mid)
            min = mid + 1
        else:
            max_weight = mid - 1

    return res

def bfs(x, y, c):
    dq = deque([x])
    visited = {i: False for i in range(1, n+1)}
    visited[x] = True
    
    while dq:
        cur = dq.popleft()

        if cur == y:
            return True
        for next, w in _map[cur]:
            if not visited[next] and w >= c:
                visited[next] = True
                dq.append(next)

    return False

n, m = map(int, read().split())

max_weight = 0
_map = {i:[] for i in range(1, n+1)}

# 1~다리의 최대 중량에서 섬 사이에 이동할 수 있는 최대 중량을 이분 탐색으로 찾음
for t in range(m):
    x, y, c = map(int, read().split())
    max_weight = max(max_weight, c)
    _map[x].append([y, c])
    _map[y].append([x, c])

s, e = map(int, read().split())
print(binary_search())