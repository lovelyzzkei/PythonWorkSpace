import sys; read = sys.stdin.readline
from collections import deque

MAX = 58
INF = sys.maxsize

c = [[0 for i in range(MAX)] for j in range(MAX)]
f = [[0 for i in range(MAX)] for j in range(MAX)]
a = {i:[] for i in range(MAX)}

def toInt(l):
    return (ord(l[0])-65, ord(l[1])-65, int(l[2]))

def maxFlow(start, end):
    result = 0

    # s-t 경로가 없을 때까지 반복
    while True: 
        prev = [-1 for i in range(MAX)]
        q = deque([])
        q.append(start)

        # 경로를 탐색하기 위한 BFS 실행
        while len(q) != 0:
            x = q.popleft()

            for i in range(len(a[x])):
                y = a[x][i] # 현재 노드에서 다음 노드

                # 방문하지 않은 노드 중 용량이 남은 경우
                if c[x][y] - f[x][y] > 0 and prev[y] == -1:
                    q.append(y)
                    prev[y] = x

                    # 경로를 찾으면 BFS 종료
                    if (y == end): 
                        break

        # 더 이상 경로가 존재하지 않는다면 while 문 종료
        if prev[end] == -1:
            break

        # AUGMENT FLOW
        # min-cut max-Flow 탐색
        flow = INF
        i = end
        while i != start:
            flow = min(flow, c[prev[i]][i] - f[prev[i]][i])
            i = prev[i]

        i = end
        # 찾은 flow 만큼 반영        
        while i != start:
            f[prev[i]][i] += flow   # forward는 +
            f[i][prev[i]] -= flow   # backward는 -
            i = prev[i]

        result += flow

    return result

# main 함수 부분
n = int(read())
for i in range(n):
    s, t, v = toInt(read().strip().split())
    a[s].append(t)
    a[t].append(s)
    c[s][t] += v
    c[t][s] += v

print(maxFlow(0, 25))