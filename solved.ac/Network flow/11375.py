import sys; read = sys.stdin.readline
from collections import deque

n, m = map(int,read().split())
INF = sys.maxsize

# 직원의 수 + 일의 수 + s,t 노드 만큼 초기화
c = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
f = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
a = {i:[] for i in range(n+m+2)}

def dfs(start, end, flow, visited):
    if visited[start]:
        return 0
    visited[start] = True

    # sink 노드 도착 -> 탈출
    if start == end:
        return flow

    for y in a[start]:
        now_flow = c[start][y] - f[start][y]
        if now_flow <= 0:
            continue

        result = dfs(y, end, now_flow, visited)
        if result:
            f[start][y] += result
            f[y][start] -= result
            return result

    return 0

def maxFlow(start, end):
    result = 0  

    while True:
        visited = [False for i in range(n+m+2)]
        flow = dfs(start, end, INF, visited)
        if not flow:
            break
        result += flow
    
    return result


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


print(maxFlow(0, n+m+1))