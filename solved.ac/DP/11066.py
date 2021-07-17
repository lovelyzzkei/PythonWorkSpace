import sys; read = sys.stdin.readline
INF = int(1e9)

T = int(read())
for tc in range(T):
    k = int(read())
    t = [0] + list(map(int, read().split()))
    dp = [INF] * (k+1); dp[0] = dp[1] = 0

    # 누적 합 리스트 생성
    cul_sum = [0] * (k+1)
    for i in range(1, k+1):
        cul_sum[i] = t[i] + cul_sum[i-1]

    for i in range(2, k+1):
        dp[i] = min(dp[i-2]+t[i-1]+t[i], dp[i-1]) + cul_sum[i]

    print(dp)