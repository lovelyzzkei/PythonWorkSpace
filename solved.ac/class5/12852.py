import sys; read = sys.stdin.readline
n = int(read())
INF = int(1e5)
dp = {i:INF for i in range(1, n+1)}; dp[1] = 0
ans = {i:[] for i in range(1, n+1)}
for i in range(1, n+1):
    if i+1 <= n and dp[i+1] > dp[i] + 1:
        dp[i+1] = dp[i] + 1
        ans[i+1].extend(ans[i])
    if i*2 <= n and dp[i*2] > dp[i] + 1:
        dp[i*2] = dp[i] + 1
        ans[i*2].extend(ans[i])
    if i*3 <= n and dp[i*3] > dp[i] + 1:
        dp[i*3] = dp[i] + 1
        ans[i*3].extend(ans[i])

print(dp[n])
print(ans[n])
