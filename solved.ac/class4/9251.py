import sys; read = sys.stdin.readline
a = read().strip()
b = read().strip()

dp = [[0] * (len(b) + 1) for i in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:        # 맨 뒤의 문자열이 같을 경우
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
print(dp[len(a)][len(b)])