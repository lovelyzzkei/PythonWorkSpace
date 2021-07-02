import sys; read = sys.stdin.readline
t = int(read())
INF = int(1e8)
a = [0] * 501
dp = [0] * 501
for tc in range(t):
    _a, _b = map(int, read().split())
    a[_a] = _b
    dp[_a] = 1
for i in range(1, 501):
    for j in range(1, i+1):
        if a[i] != 0 and a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(t-max(dp))
