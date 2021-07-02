import sys; read = sys.stdin.readline
h, y = map(int, read().split())
dp = [0] * 11; dp[0] = h
for i in range(0, 11):
    if i+1 < 11:
        dp[i+1] = max(dp[i+1], int(dp[i]*1.05))
    if i+3 < 11:
        dp[i+3] = max(dp[i+3], int(dp[i]*1.2))
    if i+5 < 11:
        dp[i+5] = max(dp[i+5], int(dp[i]*1.35))

print(dp[y])