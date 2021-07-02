import sys; read = sys.stdin.readline
n = int(read())
ans = 0
dp = [1] * (n+1);
for i in range(n):
    num = round(float(read()), 2)
    dp[i+1] = num
    ans = max(ans, num)
for i in range(1, n+1):
    if dp[i-1] > 1:
        dp[i] = dp[i-1] * dp[i]
        ans = max(ans, dp[i])
print(f'{round(ans, 3):.3f}')
