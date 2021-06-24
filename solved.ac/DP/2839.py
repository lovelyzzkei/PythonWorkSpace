import sys; read = sys.stdin.readline
dp = [-1] * 5001
dp[3] = 1; dp[5] = 1
for i in range(6, 5001):
    # 둘 다 가짓수가 존재하면 둘 중 봉지의 개수가 최소가 되는 값을 저장
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-3]+1, dp[i-5]+1)
    # 둘 중 하나만 가짓수가 존재하면 다른 하나는 -1이 저장되어 있을 것이므로 -1보다 큰 값을 저장
    elif dp[i-3] != -1 or dp[i-5] != -1:
        dp[i] = max(dp[i-3]+1, dp[i-5]+1)
print(dp[int(read())])
