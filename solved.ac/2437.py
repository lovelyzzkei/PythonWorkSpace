import sys; read = sys.stdin.readline
from collections import deque

n = int(read())
d = list(map(int, read().split()))
d = deque(sorted(d))

# 리스트에 있는 수 중 현재 양의 정수와 가장 가까운 정수부터 빼면서 확인
ans = 1; found = False
cd = [0 for i in range(n+1)]
for i in range(1, n+1):
    cd[i] = d[i-1] + cd[i-1]
p = 0

while not found:
    ans_c = ans
    while p < len(d) and d[p] <= ans:
        p += 1
    if ans_c - d[p-1] > cd[p-1] or d[0] != 1:
        found = True
    else:
        ans += 1

print(ans)
