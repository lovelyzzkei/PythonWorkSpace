import sys; read = sys.stdin.readline

# 2원짜리와 5원짜리로만 거스름돈. 동전은 무한개
# 동전의 개수가 최소가 되도록
n = int(read())
INF = int(1e7)
dp = [INF] * (n+1); dp[n] = 0
for i in range(n, 1, -1):
    if i-5 >= 0:
        dp[i-5] = min(dp[i-5], dp[i]+1)
    if i-2 >= 0:
        dp[i-2] = min(dp[i-2], dp[i]+1)
if dp[0] == INF:
    print(-1)
else:
    print(dp[0])