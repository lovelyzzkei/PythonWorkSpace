import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
d = list(map(int, read().split()))
d = deque(sorted(d))

# 리스트에 있는 수 중 현재 양의 정수와 가장 가까운 정수부터 빼면서 확인
ans = 1;  l = []
found = False
while not found:
    t = ans
    if len(d) != 0 and d[0] <= ans:
        l.append(d.popleft())
    idx = len(l) - 1
    while idx >= 0:
        if l[idx] < t:
            t -= l[idx]
            idx -= 1
        elif l[idx] == t:
            ans += 1
            break
        else:
            idx -= 1
    if idx < 0 and t > 0:
        found = True


print(ans)
