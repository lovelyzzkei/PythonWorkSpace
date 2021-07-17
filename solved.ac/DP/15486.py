import sys; read = sys.stdin.readline
n = int(read())
Ti = [0]; Pi = [0]
for i in range(n):
    t, p = map(int, read().split())
    Ti.append(t)
    Pi.append(p)

dp = [0] * (n+2)
for i in range(n, 0, -1):
    if i+Ti[i]-1 <= n:
        dp[i] = max(dp[i+Ti[i]]+Pi[i], dp[i+1], dp[i])
    else:
        dp[i] = max(dp[i], dp[i+1])

print(dp[1])