import sys; read = sys.stdin.readline
from math import sqrt

dp = {i:5 for i in range(50001)}
n = int(read())

dp[0] = 0; dp[1] = 1
root = int(sqrt(n))

for i in range(n + 1):
    for j in range(1, root+1):
        next = i + pow(j, 2)
        if next <= n:
            dp[next] = min(dp[next], dp[i] + 1)

print(dp[n])