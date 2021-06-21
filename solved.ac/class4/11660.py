import sys; read = sys.stdin.readline

n, m = map(int, read().split())
t = []
for _ in range(n):
    t.append(list(map(int, read().split())))

dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + t[i-1][j-1] - dp[i-1][j-1]

ret = []
for _ in range(m):
    y1, x1, y2, x2 = map(int, read().split())
    ans = dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]
    ret.append(ans)

print('\n'.join(str(x) for x in ret))