import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
q = deque(list(map(int, read().split())))

# 처음 우유가 딸기일 때까지 pop
while len(q) != 0 and q[0] != 0:
    q.popleft()

# 처음 우유가 딸기이면 시작
prev = 2
ans = 0
while len(q) != 0:
    x = q.popleft()
    if (prev == 2 and x == 0) or \
        (prev == 0 and x == 1) or \
            (prev == 1 and x == 2):
        ans += 1
        prev = x
    
print(ans)
