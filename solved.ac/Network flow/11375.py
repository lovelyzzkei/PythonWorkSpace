import sys; read = sys.stdin.readline
from collections import deque

n, m = map(int,read().split())
INF = sys.maxsize

# 직원의 수 + 일의 수 + s,t 노드 만큼 초기화
c = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
f = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
a = {i:[] for i in range(n+m+2)}
v = [False for i in range(n+m+2)]


def maxFlow():
    totalFlow = 0  

    while True:
        # 이전 노드를 저장할 parent 리스트 및 스택을 위한 deque
        parent = [-1 for i in range(n+m+2)]
        inQueue = [False for i in range(n+m+2)]
        parent[0] = 0
        q = deque([0])

        # 스택에 아직 노드가 존재하고 sink에 도달하지 않았다면 
        while len(q) != 0 and parent[n+m+1] == -1:
            x = q.pop()
            inQueue[x] = False
            
            # y에서 갈 수 있는 노드들을 스택에 저장
            for y in a[x]:
                if c[x][y] - f[x][y] > 0 and parent[y] == -1 and not inQueue[y]:
                    parent[y] = x
                    inQueue[y] = True
                    q.append(y)
                        
        # print(parent)
        # loop가 끝나고 sink에 도달하지 못했다면 탈출
        if parent[n+m+1] == -1:
            break

        i = n + m + 1
        while i != 0:
            f[parent[i]][i] += 1
            f[i][parent[i]] -= 1
            i = parent[i]

        totalFlow += 1
    
    return totalFlow
        

# 직원: 1 ~ n, 일: n+1 ~ n+m 으로 encoding하여 저장
for i in range(1, n+1):

    # source - 직원 edge 추가
    a[0].append(i)
    a[i].append(0)
    c[0][i] = 1

    l = list(map(int, read().split()))
    for j in l[1:]:
        c[i][j+n] = 1
        a[i].append(j+n)
        a[j+n].append(i)

# 일 - sink edge를 추가
for i in range(n+1, n+m+1):
    a[i].append(n+m+1)
    a[n+m+1].append(i)
    c[i][n+m+1] = 1

print(maxFlow())