import sys; read = sys.stdin.readline
from itertools import combinations
from collections import deque

n, m = map(int, read().split())
t = [list(map(int, read().split())) for i in range(n)]
chickens = []; cities = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if t[i][j] == 1:
            cities.append([i, j])
        elif t[i][j] == 2:
            chickens.append([i, j])

ret = int(1e7)
for i in range(m, 0, -1):
    tmp = combinations(chickens, i)
    for pair in tmp:
        ans = 0
        for city in cities:
            y2, x2 = city
            d = int(1e7)
            for store in pair:
                y1, x1 = store
                d = min(d, abs(y2-y1)+abs(x2-x1))
            ans += d
        ret = min(ret, ans)

print(ret)
