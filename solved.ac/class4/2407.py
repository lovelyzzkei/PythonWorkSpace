import sys; read = sys.stdin.readline

n, m = map(int, read().split())
dp = [1] * 101

for i in range(2, n+1):
    dp[i] = i*dp[i-1]

print(dp[n] // dp[m] // dp[n-m])