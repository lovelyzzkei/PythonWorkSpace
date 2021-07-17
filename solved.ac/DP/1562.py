import sys; read = sys.stdin.readline
n = int(read())
dp = [[0 for _ in range(5)] for __ in range(n+1)]
dp[10][0] = 1
for i in range(11, n+1):
    dp[i][0] = dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3]
    dp[i][2] = dp[i-1][0] + dp[i-1][2] + dp[i-1][3]
    dp[i][3] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] * 2
    dp[i][4] = sum(dp[i]) 

ans = 0
for i in range(10, n+1):
    ans += dp[i][4]
    # ans %= 1000000000
print(ans)
print(126461847755)