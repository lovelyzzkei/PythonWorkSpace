import sys; read = sys.stdin.readline
h, w = map(int, read().split())
INF = int(1e6)
dp = [[INF for i in range(w+1)] for j in range(h+1)]

for i in range(1, h+1):
    joi = read().strip()
    for j in range(1, w+1):
        if joi[j-1] == 'c':
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i][j-1] + 1, dp[i][j])

for i in range(1, h+1):
    for j in range(1, w+1):
        if dp[i][j] >= INF:
            print('-1', end=" ")
        else:
            print(dp[i][j], end=" ")
    print()