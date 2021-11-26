import sys; read = sys.stdin.readline
from collections import deque

n = read().strip()
q = []
for i in range(len(n)):
    q.append(int(n[i]))
q.sort(reverse=True)

if q[-1] == 0 and sum(q) % 3 == 0:
    print("".join(str(x) for x in q))
else:
    print(-1)

