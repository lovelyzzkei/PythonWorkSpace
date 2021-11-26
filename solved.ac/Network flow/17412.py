import sys; read = sys.stdin.readline
from collections import deque

MAX_P = 401
c = [[0 for i in range(MAX_P)] for j in range(MAX_P)]
f = [[0 for i in range(MAX_P)] for j in range(MAX_P)]

n, p = map(int, read().split())

a = {i:[] for i in range(n+1)}

def maxFlow():
    totalFlow = 0

    while True:
        # 이전 노드들을 저장할 큐
        parent = [-1 for i in range(n+1)]
        parent[1] = 1

        inQueue = [False for i in range(n+1)]
        q = deque([1])

        # BFS
        while len(q) != 0 and parent[2] == -1:
            x = q.popleft()
            inQueue[x] = False
            
            # 아직 방문하지 않은 노드들만 큐에 저장
            for y in a[x]:
                if c[x][y] - f[x][y] > 0 and parent[y] == -1 and not inQueue[y]:
                    q.append(y)
                    parent[y] = x
                    inQueue[y] = True
                    if y == 2:
                        break

        # print(parent)

        # 더 이상 경로가 없으면 전체 while loop 탈출
        if parent[2] == -1:
            break
        
        # flow augment 및 해당 edge 들에 대한 residual graph 생성
        i = 2
        while i != 1:
            a[i].append(parent[i])
            f[parent[i]][i] += 1
            f[i][parent[i]] -= 1
            i = parent[i]

        totalFlow += 1
    
    return totalFlow
        


for i in range(p):
    u, v = map(int, read().split())
    a[u].append(v)
    c[u][v] = 1

print(maxFlow())