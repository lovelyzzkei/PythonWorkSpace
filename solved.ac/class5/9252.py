import sys; read = sys.stdin.readline
a = ' ' + read().strip()
b = ' ' + read().strip()
dp = [[[0, ''] for i in range(len(a))] for j in range(len(b))]
lcs = [['' for i in range(len(a))] for j in range(len(b))]

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if b[i] == a[j]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = (dp[i-1][j-1][1] + b[i])
        else:
            dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0])
            if dp[i-1][j][0] >= dp[i][j-1][0]:
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][1] = dp[i][j-1][1]

print('\n'.join(str(x) for x in max(max(item for item in dp))))