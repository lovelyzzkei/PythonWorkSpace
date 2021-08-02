import sys; read = sys.stdin.readline
from collections import deque
INF = int(1e7)

n = int(read())
rgb = [list(map(int, read().split())) for i in range(n)]
# dp[i][j]: 마지막 색이 j색 일때, i번째에서의 최솟값
dp = [[0 for i in range(n)] for j in range(n)]
ans = INF

for k in range(3):  # 처음 집에 칠할 색 지정 k: 0-r, 1-g, 2-b
    for i in range(3):
        if i == k:
            dp[0][i] = rgb[0][i]
        else:
            dp[0][i] = INF

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

    for i in range(3):
        if i == k:  # 처음 색과 마지막 색이 같으면 continue
            continue
        ans = min(ans, dp[n-1][i])
    
print(ans)