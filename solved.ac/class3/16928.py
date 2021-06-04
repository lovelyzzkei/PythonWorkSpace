import sys; read = sys.stdin.readline
from collections import deque

def bfs(x):
    dq = deque([x])

    while dq:
        cur = dq.popleft()
        if cur == 100:
            return 

        for dx in range(1, 7):
            next = cur + dx
            if 0 < next <= 100:
                if board[next]:
                    next = board[next]
                if time[cur] + 1 < time[next]:
                    time[next] = time[cur] + 1
                    dq.append(next)

n, m = map(int, read().split())
board = {i: 0 for i in range(1, 101)}
time = {i:99999 for i in range(1, 101)}

for i in range(n):
    x, y = map(int, read().split())
    board[x] = y

for i in range(m):
    u, v = map(int, read().split())
    board[u] = v

time[1] = 0
bfs(1)
print(time[100])