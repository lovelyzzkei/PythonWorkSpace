import sys; read = sys.stdin.readline

n, m, r = map(int, read().split())
items = {idx+1:value for idx, value in enumerate(list(map(int, read().split())))}
INF = int(1e5)
d = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 0

for _ in range(r):
    a, b, l = map(int, read().split())
    d[a][b] = l; d[b][a] = l

for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if d[start][mid] + d[mid][end] < d[start][end]:
                d[start][end] = d[start][mid] + d[mid][end]

ans = 0
for my_area in range(1, n+1):
    tmp = 0
    for other_area in range(1, n+1):
        if d[my_area][other_area] <= m:
            tmp += items[other_area]
    ans = max(ans, tmp)

print(ans)