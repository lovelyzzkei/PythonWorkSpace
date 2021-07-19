import sys; read = sys.stdin.readline
from itertools import combinations

n, s = map(int, read().split())
t = list(map(int, read().split()))

ans = 0
for i in range(1, n+1):
    tmp = list(combinations(t, i))
    for item in tmp:
        if sum(item) == s:
            ans += 1

print(ans)