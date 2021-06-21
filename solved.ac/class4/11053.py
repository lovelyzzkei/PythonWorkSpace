import sys; read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
dp = [1] * n

# 현재 시점에서 자신 이전에 있는 수들과 비교. 
for j in range(1, n):
    for i in range(j):
        if a[j] > a[i]:     # 지금이 더 크면
            dp[j] = max(dp[j], dp[i] + 1)   # 이전의 수열에 + 1 또는 현재의 수열이 최대 길이가 된다

print(max(dp))