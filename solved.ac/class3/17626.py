import sys; read = sys.stdin.readline
import math

def four_squares(n):
    if math.sqrt(n) == n // math.sqrt(n):
        dp[n] = 1
    else:
        for i in range(1, n):
            dp[n] = min(dp[n], dp[i] + dp[n-i])



dp = [5] * 50001
dp[1] = 1; dp[2] = 2; dp[3] = 3
n = int(read())
for i in range(4, n+1):
    four_squares(i)
print(dp[n])