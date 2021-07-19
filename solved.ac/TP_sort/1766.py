import sys; read = sys.stdin.readline
import heapq

n, m = map(int, read().split())
inDegree = {i:0 for i in range(1, n+1)}
tree = {i:[] for i in range(1, n+1)}
solved = {i:False for i in range(1, n+1)}

# 위상정렬 준비
for _ in range(m):
    u, v = map(int, read().split())
    tree[u].append(v)
    inDegree[v] += 1

def tp_sort():
    q = []
    # 쉬운 문제부터 해결해야하므로 우선순위 큐를 사용
    for i in range(1, n+1):
        if inDegree[i] == 0:
            solved[i] = True
            heapq.heappush(q, i)
        
    ans = []
    while q:
        now = heapq.heappop(q)
        ans.append(now)

        for child in tree[now]:
            inDegree[child] -= 1
            if inDegree[child] == 0 and not solved[child]:
                solved[child] = True
                heapq.heappush(q, child)
        
            
    print(' '.join(str(x) for x in ans))

tp_sort()