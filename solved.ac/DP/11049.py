import sys; read = sys.stdin.readline
n = int(read()); INF = int(1e9)
dp = [[INF for _ in range(n)] for __ in range(n)]
matrix = list(list(map(int, read().split())) for i in range(n))
for i in range(n):
    dp[i][i] = 0

for dist in range(1, n):
    for x in range(n-dist):
        y = x + dist
        for k in range(x, y):
            dp[x][y] = min(dp[x][y], dp[x][k] + dp[k+1][y] + matrix[x][0]*matrix[k][1]*matrix[y][1])

print(dp[0][n-1])
