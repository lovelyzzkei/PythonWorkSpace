import sys; read = sys.stdin.readline
from collections import deque

n, m = map(int,read().split())
INF = sys.maxsize

# 직원의 수 + 일의 수 + s,t 노드 만큼 초기화
c = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
f = [[0 for i in range(n+m+2)] for j in range(n+m+2)]
a = {i:[] for i in range(n+m+2)}

def maxFlow(start, end):
    result = 0

    while True:
        prev = [-1 for i in range(n+m+2)]
        q = deque([])
        q.append(start)

        # BFS 실행
        while len(q) != 0:
            x = q.popleft()

            # 현재 노드에서 갈 수 있는 노드들 중에서
            for y in a[x]:
                
                # 방문하지 않은 노드 중 용량이 남은 경우
                if c[x][y] - f[x][y] > 0 and prev[y] == -1:
                    q.append(y)
                    prev[y] = x

                    # 경로를 찾으면 BFS 종료
                    if y == end:
                        break

        # 더 이상 경로가 없으면 종료
        if prev[end] == -1:
            break

        # AUGMENT FLOW
        # min-cut max-Flow 탐색
        flow = INF
        i = end
        while i != start:
            flow = min(flow, c[prev[i]][i] - f[prev[i]][i])
            i = prev[i]

        # 찾은 flow 만큼 반영
        i = end
        while i != start:
            f[prev[i]][i] += flow
            f[i][prev[i]] -= flow
            a[i].append(prev[i])    # residual graph 생성
            i = prev[i]

        result += flow

    return result


# 직원: 1 ~ n, 일: n+1 ~ n+m 으로 encoding하여 저장
for i in range(1, n+1):

    # source - 직원 edge 추가
    a[0].append(i)
    c[0][i] = 1

    l = list(map(int, read().split()))
    for j in l[1:]:
        c[i][j+n] = 1
        a[i].append(j+n)

# 일 - sink edge를 추가
for i in range(n+1, n+m+1):
    a[i].append(n+m+1)
    c[i][n+m+1] = 1


print(maxFlow(0, n+m+1))