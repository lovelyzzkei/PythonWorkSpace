import sys; read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n = int(read())
    t = [0] + list(map(int, read().split()))
    cul_sum = [0] * (n+2)
    dp = [0] * (n+1)

    # 누적 합 구하기
    for i in range(1, n+1):
        cul_sum[i+1] = cul_sum[i] + t[i]

    # 구간 합 구하는 함수 설정
    def sum_range(i, j):
        return cul_sum[j+1] - cul_sum[i]

    # print(t)
    print(cul_sum) 
    dp[1] = t[1]; dp[2] = t[1] + t[2]
    dp[3] = min(2*dp[2] + t[3], 2*(t[2]+t[3])+t[1])

    for i in range(4, n+1):
        dp[i] = min(2*(t[i-1]+t[i] + dp[i-2]), dp[i-1]+cul_sum[i]+t[i])

    print(dp)