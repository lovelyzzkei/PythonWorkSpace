import sys; read = sys.stdin.readline

dance = list(map(int, read().split()))[:-1]
dp = [[0 for i in range(3)] for j in range(len(dance))]
FOOT = [dance[0], 0]; dp[0][0] = dp[0][2] = 2
DDR = {1:[2, 4], 2:[1, 3], 3:[2, 4], 4:[1, 3]}

for i in range(1, len(dance)):
    step = dance[i]
    if step in FOOT:    # 같은 위치에 발이 존재
        idx = FOOT.index(step); other = (idx+1) % 2
        dp[i][idx] = dp[i-1][idx] + 1
        dp[i][other] = dp[i-1][other]
    elif 0 in FOOT:     # 중점에 발이 존재
        idx = FOOT.index(0); other = (idx+1) % 2
        dp[i][idx] = dp[i-1][idx] + 2
        dp[i][other] = dp[i-1][other]
        FOOT[idx] = step
    else:
        left = FOOT[0]; right = FOOT[1]
        if step in DDR[left]:
            FOOT = [step, right]
            dp[i][0] = dp[i-1][0] + 3
            dp[i][1] = dp[i-1][1]
        else:
            FOOT = [left, step]
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1] + 3
    dp[i][2] = dp[i][0] + dp[i][1]

print(dp[len(dance)-1][2])