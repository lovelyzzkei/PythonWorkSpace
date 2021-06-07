import sys; read = sys.stdin.readline
from collections import deque

ret = []
checkBipartite = True

def bfs(n, v):
    dq = deque([n])
    color_check = {i:0 for i in range(1, v+1)}

    color_check[n] = 1  # 처음 노드 색 칠함
    while dq:
        cur = dq.popleft(); cur_color = color_check[cur]

        for next in graph[cur]:
            if color_check[next] == 0:  # 색을 아직 칠하지 않은 경우
                color_check[next] = (-1) * cur_color    # 부모 노드와 다른 색으로 칠함
                dq.append(next)

            elif cur_color + color_check[next] != 0:    # 색이 칠해져있는데 둘이 합쳐서 0이 안되는 경우
                checkBipartite = False
                return

for t in range(int(read())):
    V, E = map(int, read().split())
    graph = {i:[] for i in range(1, V+1)}

    for e in range(E):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)

    for v in range(1, V+1):
        bfs(v, V)
        if not checkBipartite:
            ret.append("NO")
            break
    ret.append("YES")
    
print('\n'.join(ret))

