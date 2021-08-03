import sys; read = sys.stdin.readline
a = read().strip()
b = read().strip()

dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for item in dp:
    print(item)