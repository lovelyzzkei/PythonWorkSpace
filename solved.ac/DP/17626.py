import sys; read = sys.stdin.readline
from math import sqrt
n = int(read())
INF = int(1e7)
dp = [INF] * (n+1); dp[0] = 0; dp[1] = 1
for i in range(n+1):
    for j in range(1, int(sqrt(n))+1):
        if i+j*j <= n:
            dp[i+j*j] = min(dp[i+j*j], dp[i]+1)

print(dp[n])
