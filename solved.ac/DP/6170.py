import sys; read = sys.stdin.readline
dp = [[1 for i in range(2)] for j in range(46)]
for i in range(2, 46):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

ret = []
t = int(read())
for _ in range(t):
    n = int(read())
    ret.append(dp[n][0] + dp[n][1])
for idx, ans in enumerate(ret):
    print(f'Scenario #{idx+1}:\n{ans}\n')