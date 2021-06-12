import sys; read = sys.stdin.readline
from collections import deque

def bfs(a, b):
    dq = deque([a])
    visited = [0 for i in range(n+1)]
    visited[a] = 1
    step = 0

    while dq:
        qlen = len(dq)
        while qlen:
            c = dq.popleft()
            if c == b:
                print(step)
                return
            
            for next in range(c, n+1, stones[c]):
                if not visited[next]:
                    visited[next] = 1
                    dq.append(next)
            
            # 뒤로도 갈 수 있음\
            for next in range(c, 0, -stones[c]):
                if not visited[next]:
                    visited[next] = 1
                    dq.append(next)

            qlen -= 1
        step += 1

    print(-1)
    return
    
n = int(read())
stones = [0] + list(map(int, read().split()))
stones = {idx:value for idx, value in enumerate(stones)}

a, b = map(int, read().split())
bfs(a, b)