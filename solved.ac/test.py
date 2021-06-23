import sys; read = sys.stdin.readline
from collections import deque
from random import randint

n, k = map(int, read().split())

def bfs(n, k):
    visited = [False] * 100001
    visited[n] = True
    q = deque([n])
    time = 0; count = 0

    if n == k:
        return [0, 1]

    while count == 0:
        qlen = len(q)
        while qlen:
            qlen -= 1
            now = q.popleft()
            if now-1 == k or now+1 == k or now*2 == k:
                count += 1
                continue
            
            if -1<now-1 and not visited[now-1]:
                visited[now-1] = True
                q.append(now-1)
            if now+1<100001 and not visited[now+1]:
                visited[now+1] = True
                q.append(now+1)
            if now*2 < 100001 and not visited[now*2]:
                visited[now*2] = True
                q.append(now*2)
         
            
        time += 1

    return [time, count]

print('\n'.join(str(x) for x in bfs(n, k)))