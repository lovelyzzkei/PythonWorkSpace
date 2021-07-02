import sys; read = sys.stdin.readline
n = int(read())
dp = [1] * (n+1)
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10

print(dp[n] % 10)