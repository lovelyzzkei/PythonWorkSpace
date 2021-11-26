import sys; read = sys.stdin.readline
from collections import deque

MAX_V = 500

c = [[0 for i in range(MAX_V)] for j in range(MAX_V)]
f = [[0 for i in range(MAX_V)] for j in range(MAX_V)]
a = []

def bfs():
    level = [-1 for i in range(MAX_V)]
    level[S] = 0    # source의 level은 0

    q = deque([S])
    while len(q) != 0:
        x = q.pop()
        for y in a[x]:

            # 레벨 값이 설정되지 않았고, 간선에 residual이 있을 때만 이동
            if level[y] == -1 and c[x][y] - f[x][y] > 0:
                level[y] = level[x] + 1
                q.append(y)

    # sink에 도달 가능하면 True, 그렇지 않으면 False
    return level[E] != -1
