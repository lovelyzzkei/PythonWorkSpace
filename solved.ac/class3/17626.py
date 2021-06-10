import sys; read = sys.stdin.readline
from math import sqrt

dp = [5] * 50001
n = int(read())

dp[0] = 0; dp[1] = 1
root = int(sqrt(n))

for i in range(n + 1):
    for j in range(1, root+1):
        if i + pow(j, 2) <= n:
            dp[i + pow(j, 2)] = min(dp[i + pow(j, 2)], dp[i] + 1)

print(dp[n])