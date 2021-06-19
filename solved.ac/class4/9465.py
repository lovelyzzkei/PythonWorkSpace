import sys; read = sys.stdin.readline

ret = []
for _ in range(int(read())):
    n = int(read())
    t = [([0]+list(map(int, read().split()))) for j in range(2)]

    dp = [[0]*(n+1) for j in range(2)]
    dp[0][1] = t[0][1]; dp[1][1] = t[1][1]
    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + t[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + t[1][i]

    ret.append(max(max(dp[0]), max(dp[1])))
print("\n".join(str(x) for x in ret))