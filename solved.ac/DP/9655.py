import sys; read = sys.stdin.readline
INF = int(1e5)
n = int(read())
dp = [INF] * (n+1); dp[n] = 0
for i in range(n, -1, -1):
    if i-3 > -1:
        dp[i-3] = min(dp[i]+1, dp[i-3])
    if i-1 > -1:
        dp[i-1] = min(dp[i]+1, dp[i-1])

if dp[0] % 2 == 1:
    print('SK')
else:
    print('CY')