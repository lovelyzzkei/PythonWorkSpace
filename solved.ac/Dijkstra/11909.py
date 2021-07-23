import sys; read = sys.stdin.readline
INF = int(1e8)

n = int(read())
MAP = [[INF for _ in range(n+1)] for __ in range(n+1)]
tmp = [list(map(int, read().split())) for i in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        MAP[i][j] = tmp[i-1][j-1]

dp = [[0 for i in range(n+1)] for j in range(n+1)]
dp[1][1] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i, j) != (1, 1):
            l_w = 0; u_w = 0
            if MAP[i][j-1] == INF:
                l_w = INF
            if MAP[i][j-1] <= MAP[i][j]:
                l_w = MAP[i][j] - MAP[i][j-1] + 1
            if MAP[i-1][j] == INF:
                u_w = INF
            if MAP[i-1][j] <= MAP[i][j]:
                u_w = MAP[i][j] - MAP[i-1][j] + 1
            dp[i][j] = min(dp[i-1][j]+u_w, dp[i][j-1]+l_w)

print(dp[n][n])