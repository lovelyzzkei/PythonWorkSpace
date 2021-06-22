import sys; read = sys.stdin.readline

n = int(read())
t = [0] + list(map(int, read().split()))
dp = [0] * (n+1)
dp[1] = t[1]
for i in range(2, n+1):
    dp[i] = t[i] + dp[i-1]

ret = []
m = int(read())
for _ in range(m):
    i, j = map(int, read().split())
    ret.append(dp[j]-dp[i-1])

print('\n'.join(str(x) for x in ret))
