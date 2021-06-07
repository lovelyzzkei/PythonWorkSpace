import sys; read = sys.stdin.readline

INF = 1_000_000_007
dp = [0] * 4_000_001
dp[0] = 1; dp[1] = 1

def factorial(n):
    for i in range(2, n+1):
        dp[i] = (i * dp[i-1]) % INF

n, k = map(int, read().split())
factorial(n)
print(dp[n], dp[k], dp[n-k])
coefficient = (dp[n] // dp[k] // dp[n-k]) % INF
print(coefficient)