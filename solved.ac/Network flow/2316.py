import sys; read = sys.stdin.readline
from collections import deque

MAX_P = 401
c = [[0 for i in range(MAX_P)] for j in range(MAX_P)]
f = [[0 for i in range(MAX_P)] for j in range(MAX_P)]

n, p = map(int, read().split())

a = {i:[] for i in range(n+1)}
visited = [False for i in range(n+1)]

def maxFlow():
    totalFlow = 0

    while True:
        # 이전 노드들을 저장할 큐
        parent = [-1 for i in range(n+1)]
        parent[1] = 1
        q = deque([1])

        # 1, 2번 노드들은 초기화
        visited[1] = False
        visited[2] = False

        # BFS
        while len(q) != 0:
            x = q.popleft()
            
            # 2에 도달하면 break
            if x == 2:
                break
            
            # 현재 노드가 이미 방문한 노드라면 원래 edge의 canceling만 가능
            if visited[x]:
                for y in a[x]:
                    if visited[y] and (y != 1 and y != x):
                        q.append(y)
                        parent[y] = x
            else:
                for y in a[x]:
                    if c[x][y] - f[x][y] > 0 and parent[y] == -1:
                        q.append(y)
                        parent[y] = x
            print(parent, x, y)


        # 더 이상 경로가 없으면 전체 while loop 탈출
        if parent[2] == -1:
            break
        
        # flow augment 및 해당 노드들 방문 처리
        i = 2
        while i != 1:
            visited[i] = True
            f[parent[i]][i] += 1
            f[i][parent[i]] -= 1
            i = parent[i]

        totalFlow += 1
    
    return totalFlow
        


for i in range(p):
    u, v = map(int, read().split())
    a[u].append(v)
    a[v].append(u)
    c[u][v] = 1

print(maxFlow())