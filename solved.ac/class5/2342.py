import sys; read = sys.stdin.readline

dance = list(map(int, read().split()))[:-1]
DDR = {0:2, 1:0, 2:0, 3:0, 4:0}
dp = [[0 for i in range(4)] for j in range(len(dance))]
dydx = {1:[2, 4], 2:[1, 3], 3:[2, 4], 4:[1, 3]}

for i in range(len(dance)):
    step = dance[i]
    if DDR[step]:   # 해당 칸에 발이 존재
        dp[i][step] = dp[i-1][step] + 1
    elif DDR[0]:    # 중앙에 발이 존재
        DDR[0] -= 1; DDR[step] += 1
        dp[i][step] = dp[i-1][step] + 2
    else:
        flag = False
        for d in dydx[step]:
            if DDR[d]:
                DDR[d] -= 1; DDR[step] += 1
                dp[i][step] = dp[i-1][step] + 3
                flag = True
                break
        if not flag:
            pass