import sys; read = sys.stdin.readline
T = int(read())
ret = []
for tc in range(T):
    n = int(read())
    t = list(map(int, read().split()))
    
    # 누적 합 구하기
    pSum = [0] * (n+1)
    for i in range(1, n+1):
        pSum[i] = pSum[i-1] + t[i-1]
    def cul_sum(i, j):
        return (pSum[j+1]-pSum[i])
    # print(t)
    # print(pSum)

    INF = int(1e9)
    dp = [[INF for _ in range(n)] for __ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for dist in range(1, n):
        for x in range(n-dist):
            y = x + dist
            last = cul_sum(x, y)
            for k in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][k]+dp[k+1][y] + last)
    ret.append(dp[0][n-1])

print('\n'.join(str(x) for x in ret))

